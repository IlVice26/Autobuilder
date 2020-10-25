#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Autobuilder
# 
# Copyright (C) 2020 Elia Vicentini <eliavicentini26@gmail.com> 

""" Manages bash screen display """

import os
import curses
import json


class BashManager():

    def __init__(self):
        self.stdscr = curses.initscr()

        # Initial settings
        curses.start_color()
        
        # Color Pair 
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)  # First Color
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)  # Second Color

        # Other settings
        curses.noecho()
        curses.nocbreak() 
        self.stdscr.bkgd(curses.color_pair(1))
        curses.curs_set(0)

        # Window setting, dimwin[0] = y, dimwin[1] = x
        self.dimwin = self.__get_max_xy()
        self.win = self.__create_win(self.dimwin[0], self.dimwin[1])

        self.dimwinx = self.dimwin[1]
        self.dimwiny = self.dimwin[0]

        # Class variables
        self.all_facades = {}

        # Load conf file
        self.__load_conf_json()


    def __add_str_pos(self, string, pos_x, pos_y, type=""):
        """ Print a string in a specific point and refresh the window """

        if type is "bold":
            self.win.addstr(pos_x, pos_y, str(string), curses.A_BOLD)
        elif type is "italic":
            self.win.addstr(pos_x, pos_y, str(string), curses.A_ITALIC)
        elif type is "reverse":
            self.win.addstr(pos_x, pos_y, str(string), curses.A_REVERSE)
        else:
            self.win.addstr(pos_x, pos_y, str(string))


    def __add_title(self, string):
        """ Print a title """

        # Calculation of the space between the title and the borders
        title_space = self.dimwin[1] - len(string)
        if title_space % 2 == 1:
            space_left = int(title_space / 2)
            space_right = space_left + 1
        else:
            space_left = int(title_space / 2)
            space_right = int(title_space / 2)
        
        self.win.addstr(0, 0, 
            space_left * " " + str(string) + space_right * " "
            , curses.A_REVERSE)


    def __add_body(self, dict_b):
        # self.add_str_pos(str(len(dict_b) + 1), 0 , 0)
        for key in list(dict_b.keys()):
            if str(dict_b[key]).__contains__("&v&"):
                string = str(dict_b[key]).split("&v&")
                self.__add_str_pos(str(string[0]) + str(self.__get_var(string[-2])), int(key), 0)
            else:
                self.__add_str_pos(str(dict_b[key]), int(key), 0)


    def __add_footer(self, string):
        if not string == "":
            space_right = self.dimwin[1] - len(string) - 1
            self.__add_str_pos(string + " " * space_right, 
                self.dimwin[0] - 1, 0, "reverse")


    def __create_win(self, height, width):
        win = curses.newwin(height, width)
        return win


    def __get_max_xy(self):
        return self.stdscr.getmaxyx()


    def __get_var(self, source):
        return getattr(self, source)


    def __load_conf_json(self):
        """ It loads all window configs """
        
        # Loading config file
        try:
            conf_file = open("facades/config.json", "r")
            data_conf = json.load(conf_file)
            files_win = data_conf["facades"]
        except FileNotFoundError:
            self.__clear_win()
            self.__add_str_pos("The 'config.json' file has not been found...", 0, 0)
            self.win.refresh()
            self.win.getch()
            exit(-1)

        self.all_facades = {}

        # Loading every file founded in config.json
        for cf_file in files_win:
            file = open("facades/" + cf_file, "r")
            data = json.load(file)
            self.all_facades[cf_file] = data['window']


    def load_facade(self, facade_name):
        """ Load a facade chosen by the user """

        filename = facade_name + ".json"

        # Check if the file has been uploaded previously
        if filename in list(self.all_facades.keys()):
            self.__clear_win()
            self.__add_title(self.all_facades[filename]["title"])
            self.__add_body(self.all_facades[filename]["body"])
            self.__add_footer(self.all_facades[filename]["footer"])
            self.win.refresh()
            self.win.getch()
        else:
            self.__clear_win()
            self.__add_str_pos("The façade was not previously loaded." +
            " Check the name and reload the program.", 0, 0)
            self.win.refresh()
            self.win.getch()
            exit(-1)


    def __load_facade_test(self):
        filename = "test.json"
        self.__add_title(self.all_facades[filename]["title"])
        self.__add_body(self.all_facades[filename]["body"])
        self.__add_footer(self.all_facades[filename]["footer"])
        self.win.refresh()
        self.win.getch()


    def __clear_win(self):
        self.win.clear()

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
        self.dimwin = self.get_max_xy()
        self.win = self.create_win(self.dimwin[0], self.dimwin[1])

        # Class variables
        self.all_facades = {}

        # Load conf file
        self.load_conf_json()


    def add_str_pos(self, string, pos_x, pos_y, type=""):
        """ Print a string in a specific point and refresh the window """

        if type is "bold":
            self.win.addstr(pos_x, pos_y, str(string), curses.A_BOLD)
        elif type is "italic":
            self.win.addstr(pos_x, pos_y, str(string), curses.A_ITALIC)
        elif type is "reverse":
            self.win.addstr(pos_x, pos_y, str(string), curses.A_REVERSE)
        else:
            self.win.addstr(pos_x, pos_y, str(string))


    def add_title(self, string):
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


    def add_body(self, dict_b):
        # self.add_str_pos(str(len(dict_b) + 1), 0 , 0)
        for key in list(dict_b.keys()):
            self.add_str_pos(str(dict_b[key]), int(key), 0)


    def add_footer(self, string):
        if not string == "":
            space_right = self.dimwin[1] - len(string) - 1
            self.add_str_pos(string + " " * space_right, 
                self.dimwin[0] - 1, 0, "reverse")


    def create_win(self, height, width):
        """ Create and returns a new window inside a box """

        win = curses.newwin(height, width)
        return win


    def get_max_xy(self):
        return self.stdscr.getmaxyx()


    def load_conf_json(self):
        """ It loads all window configs """
        
        # Loading config file
        conf_file = open("facades/config.json", "r")
        data_conf = json.load(conf_file)
        files_win = data_conf["facades"]

        self.all_facades = {}

        # Loading every file founded in config.json
        for cf_file in files_win:
            file = open("facades/" + cf_file, "r")
            data = json.load(file)
            self.all_facades[cf_file] = data['window']


    def load_facade(self, facade_name):
        filename = facade_name + ".json"
        self.add_title(self.all_facades[filename]["title"])
        self.add_body(self.all_facades[filename]["body"])
        self.add_footer(self.all_facades[filename]["footer"])
        self.win.refresh()
        self.win.getch()


    def load_facade_test(self):
        filename = "test.json"
        self.add_title(self.all_facades[filename]["title"])
        self.add_body(self.all_facades[filename]["body"])
        self.add_footer(self.all_facades[filename]["footer"])
        self.win.refresh()
        self.win.getch()

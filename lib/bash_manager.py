#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Autobuilder
# 
# Copyright (C) 2020 Elia Vicentini <eliavicentini26@gmail.com> 

""" Manages bash screen display """

import os
import curses
from curses import wrapper


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

        # Window setting
        self.dimwin = self.get_max_xy()
        self.win = self.create_win(self.dimwin[0], self.dimwin[1])


    def add_str(self, string, type=""):
        """ Print a string and refresh the window """

        if type is "bold":
            self.win.addstr(string, curses.A_BOLD)
            self.win.refresh()
        elif type is "italic":
            self.win.addstr(string, curses.A_ITALIC)
            self.win.refresh()
        elif type is "reverse":
            self.win.addstr(string, curses.A_REVERSE)
            self.win.refresh()
        else:
            self.win.addstr(string)
            self.win.refresh()


    def add_str_pos(self, string, pos_x, pos_y, type=""):
        """ Print a string in a specific point and refresh the window """

        if type is "bold":
            self.win.addstr(pos_x, pos_y, string, curses.A_BOLD)
            self.win.refresh()
        elif type is "italic":
            self.win.addstr(pos_x, pos_y, string, curses.A_ITALIC)
            self.win.refresh()
        elif type is "reverse":
            self.win.addstr(pos_x, pos_y, string, curses.A_REVERSE)
            self.win.refresh()
        else:
            self.win.addstr(pos_x, pos_y, string)
            self.win.refresh()


    def add_title(self, string):
        """ Print a title """

        bar = " " * self.dimwin[1]

        self.win.addstr(0, 0, bar, curses.A_REVERSE)
        self.win.refresh()


    def create_win(self, height, width):
        """ Create and returns a new window inside a box """

        win = curses.newwin(height, width)
        return win


    def get_max_xy(self):
        return self.stdscr.getmaxyx()

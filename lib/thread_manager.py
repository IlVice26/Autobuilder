#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Autobuilder
# 
# Copyright (C) 2020 Elia Vicentini <eliavicentini26@gmail.com> 

""" Check and manage all threads correctly """

from threading import Thread, ThreadError
from lib.bash_manager import BashManager
import time


class ThreadManager():

    def __init__(self, bash_manager):
        self.bash = bash_manager


    def start_threads(self):
        """ Starts all the threads used by the program """

        # Testing a Thread to verify its functioning
        try:
            testing_thread = Thread(target=self.test_thread, args=()) 
            testing_thread.start()
        except ThreadError:
            self.bash.add_str(ThreadError.with_traceback())
            exit(-1)

        # Within this construct all Threads are initialised
        try:
            # Initialization of the Thread
            self.bash.load_facade("test")

            # From this point all Threads start
            pass
        except ThreadError:
            self.bash.add_str(ThreadError.with_traceback())


    def test_thread(self):
        pass

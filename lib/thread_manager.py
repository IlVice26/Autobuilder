#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Autobuilder
# 
# Copyright (C) 2020 Elia Vicentini <eliavicentini26@gmail.com> 

""" Check and manage all threads correctly """

from threading import Thread, ThreadError
import time


class ThreadManager():

    def __init__(self, bash_manager, variables_manager):
        self.bash = bash_manager
        self.variables = variables_manager


    def start_threads(self):
        """ Starts all the threads used by the program """

        """# Testing a Thread to verify its functioning
        try:
            testing_thread = Thread(target=self.test_thread, args=()) 
            testing_thread.start()
        except ThreadError:
            self.bash.add_str(ThreadError.with_traceback())
            exit(-1)
        """

        # Within this construct all Threads are initialised
        try:
            # Initialization of the Thread
            # self.bash.load_facade("test") 
            ctrl_keys = Thread(target=self.thread_ctrl_keys, args=())
            
            # From this point all Threads start
            # ctrl_keys.start()
        except ThreadError:
            self.bash.add_str(ThreadError.with_traceback())


    def thread_ctrl_keys(self):
        pass
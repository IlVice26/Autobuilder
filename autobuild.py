#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Autobuilder
# 
# Copyright (C) 2020 Elia Vicentini <eliavicentini26@gmail.com> 

""" Description """

from lib.thread_manager import ThreadManager
from lib.bash_manager import BashManager
from lib.variables_manager import VariablesManager
import os


def main():

    # Initialising all libraries
    variables_manager = VariablesManager()
    bash_manager = BashManager(variables_manager)
    thread_manager = ThreadManager(bash_manager, variables_manager)
    
    bash_manager.load_facade("main")
    thread_manager.start_threads()
    
    


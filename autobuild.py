#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Autobuilder
# 
# Copyright (C) 2020 Elia Vicentini <eliavicentini26@gmail.com> 

""" Description """

from lib.thread_manager import ThreadManager
from lib.bash_manager import BashManager
import os


def main():

    # Initialising all libraries
    bash_manager = BashManager()
    thread_manager = ThreadManager(bash_manager)

    thread_manager.start_threads()

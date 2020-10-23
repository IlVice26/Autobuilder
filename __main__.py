#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Autobuilder
# 
# Copyright (C) 2020 Elia Vicentini <eliavicentini26@gmail.com>

""" Starts Autobuilder program """

import autobuild
import os
import sys

from termios import tcflush, TCIOFLUSH


if __name__ == "__main__":
    try:
        autobuild.main()
    except KeyboardInterrupt:
        os.system("reset")
        tcflush(sys.stdin, TCIOFLUSH)
    finally:
        os.system("reset")
        tcflush(sys.stdin, TCIOFLUSH)

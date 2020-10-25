#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# Autobuilder
# 
# Copyright (C) 2020 Elia Vicentini <eliavicentini26@gmail.com> 

class VariablesManager():
    
    def __init__(self):
        self.enable_keyboard = False

    def get_keyboard(self):
        return self.enable_keyboard

    def set_keyboard(self, status):
        self.enable_keyboard = status
    
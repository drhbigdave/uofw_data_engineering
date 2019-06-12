#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 14:19:10 2019

@author: davidhagan

Scopes demo
"""

count = 0

def show_count():
    print("count = ", count)
    
    
def set_count(c):
    global count
    count = c
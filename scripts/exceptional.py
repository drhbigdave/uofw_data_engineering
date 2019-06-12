#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 18:06:48 2019

@author: davidhagan
"""
import sys
from math import log

def convert(s):
    '''convert to integer'''
    try:
        return(int(s))
    except (ValueError,TypeError) as e:
        print("Conversion error: {}"\
              .format(str(e)),file=sys.stderr)
        raise


def string_log(s):
    v = convert(s)
    return(log(v))
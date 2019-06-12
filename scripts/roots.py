#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 18:35:07 2019

@author: davidhagan
"""
import sys

def sqrt(x):
    '''Compute square roots using the method of Heron of Alexandria
    
    Args:
        x: for the number of which will be square rooted
        
    Returns:
        the square root of x
    '''
    if x < 0:
        raise ValueError(f"Cannot compute the square root of negative number {x}")
    
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x /guess)/2.0
        i += 1
    return(guess)
    
def main():
    try:
        print(sqrt(9))
        print(sqrt(2))
        print(sqrt(-1))
        print('this is never printed')
    except ValueError as e:
        print(e, file=sys.stderr)
    print('exits as it should')
    
if __name__ == '__main__':
    main()
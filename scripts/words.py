#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 16:11:35 2019

@author: davidhagan

Retrieve and print words from a URL

Usage:
    python3 words.py <URL>
"""
from urllib.request import urlopen
import sys

def fetch_words(url):
    '''Fetch a list of words from a URL
    
    Args: 
        url: the URL of a utf-8 encoded text document
    
    Returns:
        A list of strings of words obtained from the 
        text document.
    '''
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return(story_words)
 
    
def print_items(items):
    '''Print items one per line.
    
    Args:
        an iterable series of printable items
    '''
    for item in items:
        print(item)
 
       
def main(url):
    words = fetch_words(url)
    print_items(words)
    ''' Print a list of words from a URL
    
    Args:
        url:  url: the URL of a utf-8 encoded text document
    '''

    
if __name__ == '__main__':
    main(sys.argv[1]) # 0 or zero is the filename arg so you must use 1
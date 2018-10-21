#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def UI_input_string() -> str:
    '''Function input string'''
    currString = input("Enter some string ")
    currString = currString.split(" ")
    return currString

def UI_print_result(result: list):
    '''prints result'''
    print(*map(lambda s: s[0],result))

def find_min_len(currString: list) -> str:
    wordsLength = map(lambda x: len(x), currString)
    zipped = zip(currString, wordsLength)
    sortedString = sorted(zipped, key = lambda s: s[1])
    return sortedString

UI_print_result(find_min_len(UI_input_string()))

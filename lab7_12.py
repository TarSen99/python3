#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def UI_input_string() -> str:
    '''Function input string'''
    currString = input("Enter some string ")
    return currString

def UI_print_result(result: list):
    '''prints result'''
    print(result)

def remove_spaces(currStr: str) -> str:
    withoutSpaces = ''
    nextSpace = False
    for i in range(len(currStr)):
        if currStr[i] == ' ':
            nextSpace = True
        else:
            if nextSpace:
                withoutSpaces += ' ' + currStr[i]
                nextSpace = False
            else:
                withoutSpaces += currStr[i]
    return withoutSpaces
  

UI_print_result(remove_spaces(UI_input_string()))

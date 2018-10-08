#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def UI_input_string() -> str:
    '''Function input string'''
    printString = input("Enter some string ")
    return printString


def print_string(starsString: str):
    '''Function print string with stars'''
    print("*" * (len(starsString) + 4))
    print("* " + starsString + " *")
    print("*" * (len(starsString) + 4))

print_string(UI_input_string())

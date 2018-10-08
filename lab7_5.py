#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def UI_input_string() -> str:
    '''Function input string'''
    printString = input("Enter some string ")
    return printString

def UI_output_count(count: int):
    '''Function prints count of loud letters'''
    print("Count is " + str(count))


def loud_letters_count(currString: str) -> int:
    '''Function returns count of loud letters'''
    loud = ['a', 'o', 'u', 'i', 'e', 'y']
    return sum(currString.count(i) for i in loud)

UI_output_count(loud_letters_count(UI_input_string()))

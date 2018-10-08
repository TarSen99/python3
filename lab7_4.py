#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def UI_input_string() -> str:
    '''Function input string'''
    checkString = input("Enter some string ")
    return checkString

def UI_output_result(resultString: str):
    '''Function output result'''
    print("Encrypt word is " + resultString)

def string_crypt(checkString: str) -> str:
    '''Crypt string'''
    cryptString = ""
    for _ in checkString:
        cryptString += get_neighbor_letter(_)
    return cryptString

def get_neighbor_letter(currLetter: str) -> str:
    '''get neighbor letter'''
    if ord(currLetter) == ord('z'):
        return 'a'
    return chr(ord(currLetter) + 1)

UI_output_result(string_crypt(UI_input_string()))
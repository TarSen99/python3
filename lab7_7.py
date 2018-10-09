#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def UI_input_string() -> str:
    '''Function input string'''
    enterString = input("Enter some string ")
    return enterString

def UI_output_result(result: str):
    '''Function prints result string'''
    print(result)

def check_type(enterString: str) -> str:
    '''check type of string'''
    result = ''
    for i in enterString:
        if i.isupper():
            result = to_camel_case(enterString)
            break
        elif i == "_":
            result = to_snake_case(enterString)
            break
        else:
            result = enterString
    return result

def to_camel_case(enterString: str) -> str:
    '''Function changes str to camel_case'''
    finalString = ''
    for i in enterString:
        if i.isupper():
            finalString += "_" + i.lower()
        else:
            finalString += i
    return finalString

def to_snake_case(enterString: str) -> str:
    '''Function changes str to snakeCase'''
    finalString = ''
    nextUpper = False
    for i in enterString:
        if i == "_":
            nextUpper = True
        else:
            if nextUpper:
                finalString += i.upper()
                nextUpper = False
            else:
                finalString += i
    return finalString
            
UI_output_result(check_type(UI_input_string()))

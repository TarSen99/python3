#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def UI_input_count() -> int:
    '''This function input length of string needs to be moved'''
    moveCount = int(input("Enter some length to move "))
    return moveCount

def UI_input_string() -> str:
    '''Function input string'''
    moveString = input("Enter some string ")
    return moveString

def string_move(moveString: str, moveCount: int) -> str:
    '''Function moves characters of string'''
    if moveCount > 0:
        finalString = moveString[-moveCount:] + moveString[:-moveCount]
    else:
        finalString = moveString[abs(moveCount):] + moveString[:abs(moveCount)]
    return finalString

def UI_output(finalString: str):
    '''Function prints the result'''
    print(finalString)

UI_output(string_move(UI_input_string(), UI_input_count()))
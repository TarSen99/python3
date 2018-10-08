#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def UI_input_string() -> str:
    '''Function input string'''
    checkString = input("Enter some string ")
    return checkString

def UI_print_result(result: bool):
	'''Print result'''
	if result:
	    print("String is correct")
	else:
		print("String is NOT correct")

def remove_characters(checkString: str) -> str:
    '''Remove all characters except brackets'''
    brackets = ['(', ')', '{', '}', '[', ']', '<', '>']
    for _ in checkString:
        if _ not in brackets:
            checkString = checkString.replace(_, "")
    return checkString

def check_brackets(checkString: str) -> str:
    '''check if correct couples of brackets exist'''
    print(checkString)
    brackets = ['()', '{}', '[]', '<>']
    while len(checkString) > 0:
        startLen = len(checkString)
        for _ in brackets:
            if _ in checkString:
                checkString = checkString.replace(_, "")
            if len(checkString) == 0:
                return True
        if startLen == len(checkString):
            break
    return False

UI_print_result(check_brackets(remove_characters(UI_input_string())))
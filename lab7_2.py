#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def UI_input_string() -> str:
    '''Function input string'''
    checkString = input("Enter some string ")
    return checkString

def UI_print_result(result: bool):
	'''Print result'''
	if result:
	    print("String is palindrome")
	else:
		print("String is NOT palindrome")

def remove_symbols(checkString: str) -> str:
    '''remove specail characters'''
    symbols = [" ", ",", "\'", "-", "+", "_"]
    lowerString = checkString.lower()
    for _ in lowerString:
        if _ in symbols:
            lowerString = lowerString.replace( _ , "")
    return lowerString

def check_inverse_string(checkString: str) -> str:
    '''get reverse string'''
    if checkString == checkString[::-1]:
        return True
    else:
    	return False

UI_print_result(check_inverse_string(remove_symbols(UI_input_string())))
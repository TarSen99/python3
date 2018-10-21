#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def UI_input_string() -> str:
    '''Function input string'''
    email = input("Enter some string ")
    return email

def UI_print_result(result: bool):
    '''prints result'''
    if result:
        print("e-mail is valid")
    else:
        print("e-mail is not valid")

def check_email_valid(email: str) -> str:
    if re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$",
     email):
        return True
    else:
        return False
  

UI_print_result(check_email_valid(UI_input_string()))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import string

def UI_print_result(result: str):
    '''prints result'''
    print(result)

def pwd():
    
    pwd = ""
    count = 0
    length = 8

    while count != length:

        upper = [random.choice(string.ascii_uppercase)]
        lower = [random.choice(string.ascii_lowercase)]
        num = [random.choice(string.digits)]
        symbol = [random.choice(string.punctuation)]
        everything = upper + lower + num + symbol

        pwd += random.choice(everything)
        count += 1

        if count == length:
            return pwd
  

UI_print_result(pwd())

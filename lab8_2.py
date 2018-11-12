#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

def set_size() -> int:
    '''inputs size'''
    size = int(input("Enter size of list "))
    return size
def print_sorted(currList: list):
    '''print sorted list'''
    print(currList)

def generate_list(size: int) -> list:
    '''generate list'''
    currList = [random.randint(1,30) for currList in range(size)]
    return currList

def sort_list(currList: list) -> list:
    '''sort list'''
    for _ in range(len(currList)-1,0,-1):
        for i in range(_):
            if currList[i]>currList[i+1]:
                temp = currList[i]
                currList[i] = currList[i+1]
                currList[i+1] = temp
    return currList

print_sorted(sort_list(generate_list(set_size())))
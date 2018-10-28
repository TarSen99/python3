#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def set_size() -> int:
    '''inputs size'''
    size = int(input("Enter size of list "))
    return size

def set_step() -> int:
    '''inputs step'''
    step = int(input("Enter step "))
    return step

def create_list(size: int) -> list:
    '''creates list'''
    currList = [i+1 for i in range(size)]
    return currList

def print_result(el: int):
    '''print result'''
    print("The last value is " + str(el))

def remove_elements(currList: list, step: int) -> int:
    prevPos = 0
    iterr = 1
    while len(currList) > 1:
        if prevPos == len(currList):
            prevPos = 0
        if iterr == step:
            removable = currList[prevPos]
            currList.remove(removable)
            if prevPos == len(currList):
                prevPos = 0
        if iterr == step:
            iterr = 1
        prevPos += 1
        iterr += 1

    return currList[0]
    
print_result(remove_elements(create_list(set_size()), set_step()))
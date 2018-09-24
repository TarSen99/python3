#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('Enter 2 dimensions of the door')

width = int(input())
height = int(input())

print('Enter 3 dimensions of the box')

a = int(input())
b = int(input())
c = int(input())

exist = False

if (width > a and height > b) or (width > b and height > a):
    exist = True
elif (width > a and height > c) or (width > c and height > a):
    exist = True
elif (width > b and height > c) or (width > c and height > b):
    exist = True
else:
    print('box doesnt exist')
    
if exist:
    print('box exist')

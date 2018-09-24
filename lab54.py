#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('Enter a,b,c')

a = int(input())
b = int(input())
c = int(input())

d = (( b )**2 ) - 4 * a * c

print("D= " + str(d))

if d == 0:
    if a != 0:
        x1 = ( -1 * b ) / 2 * a
        x2 = x1
        print('x1 is ' + str(x1))
        print('x2 is ' + str(x2))
    else:
        if b != 0:
            x1 = ( -1 * c ) / b
            x2 = x1
            print('x1 is ' + str(x1))
            print('x2 is ' + str(x2))
        else:
            if c == 0:
                x1 = 0
                x2 = 0
                print('x1 is ' + str(x1))
                print('x2 is ' + str(x2))
            else:
                print('No roots')
elif d > 0:
    if a != 0:
        x1 = (( -1 * b ) - ((b)**2 - 4 * a * c)**(1/2))/ (2 * a)
        x2 = (( -1 * b ) + ((b)**2 - 4 * a * c)**(1/2))/ (2 * a)
        print('x1 is ' + str(x1))
        print('x2 is ' + str(x2))
    else:
        print('No roots')
elif d < 0:
     if a != 0:
        x1 = (( -1 * b ) - ((b)**2 - 4 * a * c)**(1/2))/ (2 * a)
        x2 = (( -1 * b ) + ((b)**2 - 4 * a * c)**(1/2))/ (2 * a)
        print('x1 is ' + str(x1))
        print('x2 is ' + str(x2))
     else:
        print('No roots')


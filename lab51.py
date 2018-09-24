#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("Enter integer number > 0")
a = int(input())
c = int(a & (a-1))
if c == 0:
    print('true')
else:
    print('false')
    

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

print("Enter 3 real numbers")
x = float(input())
m = float(input())
o = float(input())

value = 1/(o * math.sqrt(2 * math.pi)) * math.exp(-1 * ((x - m)**2) / (2 * o**2))

print("Result is " + str(value))

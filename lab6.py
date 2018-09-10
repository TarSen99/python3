#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("Enter your height in m")
height = input()
print("Enter your weight kg")
weight = input()
weightIndex = float(weight)/float(height)**2
print("Your index is " + str(weightIndex))

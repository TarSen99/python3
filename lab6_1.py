#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = int(input("Enter side a "))
b = int(input("Enter side b "))
c = int(input("Enter side c "))

def findArea(a: int, b: int, c: int) -> float:
	"""This function gets 3 sides of triangle and calc area"""
	halfOfPerimeter = (a + b + c) / 2
	s = (halfOfPerimeter * (halfOfPerimeter - a) * (halfOfPerimeter - b) * (halfOfPerimeter - c))**(1/2)
	return s

area = findArea(a, b, c)
print("The area of triangle is " + str(area))
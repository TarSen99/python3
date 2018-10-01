#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sidesInput() -> list:
    """This function read 3 sides of triangle and return list of them"""
    a = float(input("Enter side a "))
    b = float(input("Enter side b "))
    c = float(input("Enter side c "))
    return [a, b, c]

def areaOutput(area: float):
    """This function gets value of area and print it"""
    print("The area of triangle is " + str(area))

def findArea(sides: list) -> float:
    """This function gets list of sides and calc area"""
    halfOfPerimeter = (sides[0] + sides[1] + sides[2]) / 2
    s = (halfOfPerimeter * (halfOfPerimeter - sides[0]) * (halfOfPerimeter - sides[1]) * 
    (halfOfPerimeter - sides[2]))**(1/2)
    return s

areaOutput(findArea(sidesInput()))

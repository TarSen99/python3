#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def infoInput() -> list:
   """This function gets values from user input"""
   currentMoneyAmount = float(input("Enter your current amount of money "))
   requireAmount = float(input("Enter your require amount of money "))
   yearPercent = float(input("Enter year percent for deposit "))
   return [currentMoneyAmount, requireAmount, yearPercent]

def infoOutput(yearsAmount: float):
    """Print years for deposit"""
    print("Your deposit needs years " + str(yearsAmount))

def yearsCalc(currentMoneyAmount: float, requireAmount: float, yearPercent: float) -> float:
    """This function calculate years needed to get require amount of money"""
    yearsAmount = 0
    while currentMoneyAmount < requireAmount:
    	currentMoneyAmount += getRevenuePerYear(currentMoneyAmount, yearPercent)
    	yearsAmount += 1
    return yearsAmount

def getRevenuePerYear(currentMoneyAmount: float, yearPercent: float) -> float:
    """This function return revenue per year"""
    return currentMoneyAmount / 100 * yearPercent

infoOutput(yearsCalc(*infoInput()))
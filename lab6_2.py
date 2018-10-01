#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def infoInput() -> list:
   """This function gets values from user input"""
   moneyAmount = float(input("Enter your amount of money "))
   yearPercent = float(input("Enter your percent per year "))
   yearsAmount = float(input("Enter amount of years for deposit "))
   return [moneyAmount, yearPercent, yearsAmount]

def infoOutput(moneyAmount: float):
    """Print money amount"""
    print("Your final amount of money is " + str(moneyAmount))

def depositCalc(moneyAmount: float, yearPercent: float, yearsAmount: float) -> float:
    """This function calculate sum of deposit after set count of years"""
    while yearsAmount > 0:
    	moneyAmount += getRevenuePerYear(moneyAmount, yearPercent)
    	yearsAmount -= 1
    return moneyAmount

def getRevenuePerYear(curSum: float, yearPercent: float) -> float:
    """This function return revenue per year"""
    return curSum / 100 * yearPercent

infoOutput(depositCalc(*infoInput()))
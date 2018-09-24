#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

print("Enter your choice: rock - 0, Scissors - 1, paper - 2")

humChoice = int(input())

aiChoice = random.randint(0, 2)
print('AI choise is ' + str(aiChoice))

if humChoice == aiChoice:
    print('It\'s a draw')
elif (humChoice == 0 and aiChoice == 2):
    print('You lose')
elif (humChoice == 1 and aiChoice == 0):
	print('You lose')
elif (humChoice == 2 and aiChoice == 1):
    print('You lose')
else:
    print('You win')
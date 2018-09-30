#!/usr/bin/python3


a = int(input('Enter side a '))
b = int(input('Enter side b '))
c = int(input('Enter side c '))

exist = True

if a + b < c:
    exist = False
elif a + c < b:
    exist = False
elif c + b < a:
    exist = False

if exist:
    print("Such triangle exist")
else:
    print("Such triangle can\'t exist")

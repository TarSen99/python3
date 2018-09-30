#!/usr/bin/python3


num = int(input('Enter number for cheking '))

n = 2  
isSimple = True

while n < num:
    if num % n == 0:
        isSimple = False
        break
    n = n + 1
 
if isSimple:
	print('Your number is simple')
else:
	print('Your number is not simple')

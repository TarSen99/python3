#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

print("Print two rel numbers a>=0 and b>0")
numberA = input ()
numberB = input()
numberA = float(numberA)
numberB = float(numberB)
div = (math.sqrt(numberA * numberB) / (math.exp(numberA) * numberB))
numberX = div + numberA * math.exp(2*numberA/numberB)
print("result is " + str(numberX))

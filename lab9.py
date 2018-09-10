#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from decimal import *

print("Enter your month salary")
salary = input()
tax = Decimal(salary) / Decimal(100) * Decimal(19.5)

print("Your tax is " + str(tax))

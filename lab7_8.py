#!/usr/bin/env python3
# -*- coding: utf-8 -*-
      
a = [((not (i % 3)) * 'Fizz' + (not (i % 5)) * 'Buzz') or i
for i in range(1, 100)]

print(*a)

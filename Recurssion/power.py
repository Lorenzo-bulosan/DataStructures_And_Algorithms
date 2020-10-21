# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 07:42:42 2020

@author: loren
"""

# Power of a base to the exponent using recursion
# power(2,0) // 1
# power(2,2) // 4
# power(2,4) // 16

def power(base,exponent):
    
    if (exponent == 0):
        return 1
    else:
        return base * power(base, exponent-1)

def test(real,toCheck):
    if (real == toCheck):
        return print('Pass')
    else:
        return print('Fail')

base = 0
exponent = 1

test(base**exponent, power(base,exponent))
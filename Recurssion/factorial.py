# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 08:18:19 2020

@author: loren
"""

#factorial(1) // 1
#factorial(2) // 2
#factorial(4) // 24
#factorial(7) // 5040

def factorial(n):
   
    if (n == 0):
        return 1
    else:
        return n*factorial(n-1)

def fact(n):
    
    total = 1;
    if (n == 0):
        return total    
    for i in range (1, n+1):
        total = total*i
    return total

def test(real,toCheck):
    if (real == toCheck):
        return print('Pass')
    else:
        return print('Fail')
    
# Test factorial solution against iterative
n = 3
test(fact(n),factorial(n))


# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 08:34:42 2020

@author: loren
"""

# productOfArray([1,2,3]) // 6
# productOfArray([1,2,3,10]) // 60

def productOfArray(array):
    
    length = len(array)

    if (length == 1):
        return array[0]
    else:
        return array[0]*productOfArray(array[1:])

array = [1,2,3,4]
print(productOfArray(array))
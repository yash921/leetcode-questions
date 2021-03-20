#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 17:23:40 2020

@author: yash
"""

def findAllMissingNumber(array):
    i, n = 0, len(array)
    array = sorted(array)
    while i < n:
        j = array[i] - 1
        if array[i] != array[j]:
            array[i], array[j] = array[j], array[i]
        else:
            i += 1
    print(array)
    mixingArray = []
    for i in range(len(array)):
        if array[i] != i + 1:
            mixingArray.append(i + 1)
    return mixingArray
    # array.sort()
    # for i in range(1, len(array)):
        
    
print(findAllMissingNumber([2, 3, 1, 8, 2, 3, 5, 1]))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 17:55:37 2020

@author: yash
"""

# Find the Missing Number
def findTheMissingNumber(array):
    i, n = 0, len(array)
    while i < n:
        j = array[i]
        if array[i] < n and array[i] != array[j]:
            array[i], array[j] = array[j], array[i]
        else:
            i += 1
    
    for i in range(n):
        if array[i] != i:
            return i
    return n


print(findTheMissingNumber())
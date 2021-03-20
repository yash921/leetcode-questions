#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 15:18:03 2020

@author: yash
"""

def findTheCorruptPair(array):
    i, n = 0, len(array)
    while i < n:
        j = array[i]-1
        if array[i] != array[j]:
            array[i], array[j] = array[j], array[i]
        else:
            i += 1
    
    for i in range(len(array)):
        if array[i] != i + 1:
            return [array[i], i+1]
    return -1

print(findTheCorruptPair([3, 1, 2, 3, 6, 4]))
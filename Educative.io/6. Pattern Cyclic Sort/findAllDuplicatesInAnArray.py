#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 11:39:26 2020

@author: yash
"""

def findAllDuplicatesInAnArray(array):  
    i, n = 0, len(array)
    while i < n:
        j = array[i] - 1
        if array[i] != array[j]:
            array[i], array[j] = array[j], array[i]
        else:
            i += 1
    duplicates = []
    for i in range(len(array)):
        if array[i] != i+1:
            duplicates.append(array[i])
    return duplicates

print(findAllDuplicatesInAnArray([4,3,2,7,8,2,3,1]))
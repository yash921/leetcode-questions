#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 20:45:27 2020

@author: yash
"""
# 75. Sort Colors


# Time O(n) Space O(1)
def DutchNationalFlagProblem(array):
    low = 0
    high = len(array) - 1
    i = 0
    while i <= high:
        if array[i] == 0:
            array[i], array[low] = array[low], array[i]
            i += 1
            low += 1
        elif array[i] == 1:
            i+=1
        else:
            array[i], array[high] = array[high], array[i]
            high -= 1
        
    return array

print(DutchNationalFlagProblem([1,0,2,1,0]))
    
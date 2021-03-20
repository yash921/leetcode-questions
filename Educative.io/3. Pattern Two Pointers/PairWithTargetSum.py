#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 19:05:15 2020

@author: yash
"""

def PairWithTargetSum(array, targetSum):
    
    #Solution - Two Pointers 
    #Time O(n) | Space O(1)
    # left = 0
    # right = len(array) - 1
    # while left < right:
    #     tempSum = array[left] + array[right]
    #     if targetSum == tempSum:
    #         return [array[left], array[right]]
    #     elif tempSum < targetSum:
    #         left += 1
    #     else:
    #         right -= 1
    # return -1 
    
    #Solution - Hash Map
    #Time O(n) | Space O(n)
    freq = {}
    for i, element in enumerate(array):
        if (targetSum - element) in freq:
            return [targetSum-element, element]
        else:
            freq[element] = True
print(PairWithTargetSum([1, 2, 3, 4, 6], 10))
            
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 08:27:28 2020

@author: yash
"""

def findTheSmallestMissingPositiveNumber(nums):
    i, n = 0, len(nums)
    while i < n:
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    
    for i in range(n):
        if nums[i] != i+1:
            return i + 1
    return [nums] + 1
    
print(findTheSmallestMissingPositiveNumber([1,2,3]))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 16:18:19 2020

@author: yash
"""

def maxProduct(nums):
    FirstNo = nums[0]
    ans = FirstNo * nums[1]
    for i in range(1, len(nums)-1):
        if nums[i] > 0:
            ans = max(ans, ans + nums[i] * nums[i+1])
    return ans

print(maxProduct([2,3,-2,4,5]))
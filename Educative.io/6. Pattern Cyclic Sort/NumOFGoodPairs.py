#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 15:58:55 2020

@author: yash
"""
#leetcode
def NumOFGoodPairs(nums):
    freq = {}
    for i in nums:
        if i not in freq:
            freq[i] = 0
        freq[i] += 1
    ans = 0     
    for i in freq:
        ans += (freq[i] *(freq[i] - 1))//2
    return ans

print(NumOFGoodPairs([1,2,3]))
        
        
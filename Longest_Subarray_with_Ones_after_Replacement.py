#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 19:11:33 2020

@author: yash
"""
# 1004. Max Consecutive Ones III
# Example 1:

# Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# Output: 6
# Explanation: 
# [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

# Example 2:

# Input: A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# Output: 10
# Explanation: 
# [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

# O(N) Time | O(1) Space
def Longest_Subarray_with_Ones_after_Replacement(nums, k):
    window_start = 0
    max_length = 0
    max_ones_count = 0
    for window_end in range(len(nums)):
        if nums[window_end] == 1:
            max_ones_count += 1
        
        if (window_end - window_start + 1 - max_ones_count) > k:
            if nums[window_start] == 1:
                max_ones_count -= 1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length

print(Longest_Subarray_with_Ones_after_Replacement([1,1,1,1,0,0,1,1], 1))

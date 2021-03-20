#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 17:28:38 2020

@author: yash
"""

def findTheFirst_Kth_MissingPositiveNumbers(nums, k=None):
    i , n = 0, len(nums)
    while i < n:
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
    matched = []
    for i in range(n):
        if nums[i] != i + 1 and len(matched) <= k:
            matched.append(i+1)
        elif k - len(matched) == 1:
            matched.append(nums[len(nums)-1] + 1)
    return matched
    


# n = int(input())
# if n > 0:
#     print(n)
# else:
#     s = str(n)
#     if s[len(s)-1] < s[len(s)-2] and s[len(s)-2] != '0':
#         print(int(s[:len(s)-2] + s[len(s)-1:]))
#     elif s[len(s)-1] > s[len(s)-2] and s[len(s)-1] != '0':
#         print(int(s[:len(s)-1]))
#     else:
#         print(int(s[:len(s)-1]))
print(findTheFirst_Kth_MissingPositiveNumbers([2, 3, 4], 3))
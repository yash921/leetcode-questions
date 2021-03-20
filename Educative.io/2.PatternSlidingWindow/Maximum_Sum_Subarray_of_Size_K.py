#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:43:31 2020

@author: yash
"""

#Solution - 1:

#Brute-force
# O(N * K) Time | O(1) Space
# def MaximumsumSubarrayofSizeK(array, k):
#     max_sum = 0
#     window_sum = 0
#     for i in range(len(array) - k + 1):
#         window_sum = 0
#         for j in range(i, i+k):
#             window_sum += array[j]
#             max_sum = max(max_sum, window_sum)
#     return max_sum

#Solution - 2:
#Sliding_Window
# O(N) time | O(1) Space   
def MaximumsumSubarrayofSizeK(array, k):
    max_sum, window_sum = 0, 0
    window_Start = 0
    for windowEnd in range(len(array)):
        window_sum += array[windowEnd]
        
        if windowEnd >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= array[window_Start]
            window_Start += 1
    return max_sum

print(MaximumsumSubarrayofSizeK([2, 1, 5, 1, 3, 2,5], 3))

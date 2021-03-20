#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 17:49:18 2020

@author: yash
"""

#Input: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
# Output: [2.2, 2.8, 2.4, 3.6, 2.8]

#Solution - 1

#Brute-Force
# O(N * K) Time | O(k) Space
# def avgArray(array, k):
#     avgList = []
#     for i in range(len(array) - k + 1):
#         _sum = 0.0
#         for j in range(i, i+k):
#             _sum += array[j]
#         avgList.append(_sum / 5)
#     return avgList


#Solution - 2

#Sliding_Window
# O(N) time | O(k) Space
def avgArray(array, k):
    avgList = []
    windowSum, windowStart = 0.0, 0
    for windowEnd in range(len(array)):
        windowSum += array[windowEnd]
        
        if windowEnd >= k - 1:
            avgList.append(windowSum / k)
            windowSum -= array[windowStart]
            windowStart += 1
    return avgList

print(avgArray([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))
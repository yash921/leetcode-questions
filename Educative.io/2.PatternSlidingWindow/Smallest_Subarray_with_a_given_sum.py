#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 15:57:35 2020

@author: yash
"""
import math

# 209. Minimum Size Subarray Sum


#O(N + N) Time | O(1) Space
def Smallest_Subarray_with_a_given_sum(array, RequiredSum):
    window_sum = 0
    # min_length = float("inf")
    min_length = math.inf
    window_start = 0
    for windowEnd in range(len(array)):
        window_sum += array[windowEnd]
        
        while window_sum >= RequiredSum:
            min_length = min(min_length, windowEnd - window_start + 1)
            window_sum -= array[window_start]
            window_start += 1
    if min_length == math.inf:
        return 0
    return min_length

def main():
    print(Smallest_Subarray_with_a_given_sum([2, 1, 5, 2, 3, 2],7 ))
main()
    
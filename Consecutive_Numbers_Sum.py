#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 12:52:00 2020

@author: yash
"""

#829. Consecutive Numbers Sum
#Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

# Example 1:

# Input: 5
# Output: 2
# Explanation: 5 = 5 = 2 + 3

#Solution  
def consecutiveNumberSum(N):
    count = 0
    n = 2
    while 2*N + n - n**2 > 0:
        a = (2*N + n - n**2) / (2*n)
        if a - int(a) == 0:
            # print(a, n)
            count+=1
        n+=1
    return count

print(consecutiveNumberSum(5))
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 23:43:32 2020

@author: yash
"""

#231. Power of Two

#Solution-1-Takes too much Time!!
# def powerofTwo(n):
#     while n % 2 == 0:
#         n = n/2
#     return n == 1

#Solution-2-takes less time than solution 1
# def powerofTwo(n):
#     if n == 0:
#         return True
#     return n & (-n) == n

#Solution-3-Best Solution
def powerofTwo(n):
    i = 0
    val = 1
    while val < n: #n = 4
        i+=1       #i = 1
        val = 2**i #val = 2
    if val == n:
        return True
    return False

print(powerofTwo(6))
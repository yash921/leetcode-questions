#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 10:44:32 2020

@author: yash
"""
##Given an array of integers, find the index such that the sum of all
##elements to its left and right are equal.
def quilibriumPoint(arr):
    """
    Time = O(n) | Space = O(1)
    """
    Sum = 0
    leftsum = 0
    for i in range(len(arr)):
        Sum+=arr[i]
    for i in range(len(arr)):
        Sum-=arr[i]
        if leftsum == Sum:
            print(i)
        leftsum+=arr[i]
        
quilibriumPoint([1,2,3,3])
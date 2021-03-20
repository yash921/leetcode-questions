#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 10:50:59 2020

@author: yash
"""

def findKthPositive(arr, k):
    temp = []
    for i in range(1, arr[len(arr)-1]):
        if i not in arr:
            temp.append(i)
    if len(temp) == 0:
        return arr[len(arr)-1] + k
    else:
        return temp[k-1]
                
        
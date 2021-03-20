#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 17:44:41 2020

@author: yash
"""

# Cyclic Sort

def cyclicSort(arr):
    i = 0
    while i < len(arr):
        j = arr[i] - 1
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1
    return arr[-1]

print(cyclicSort([1,1,2]))
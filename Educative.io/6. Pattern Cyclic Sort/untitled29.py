#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 15:41:47 2020

@author: yash
"""

n, k = map(int, input().split())
if k < n // 2:
    i = 1
    j = 1
    while i < n:
        if j == k:
            print(i)
        i += 2
        j += 1
else:
    if k % 2 != 0:
        k = abs((n//2)-k)  #{1, 3, 5, 7, 2, 4, 6, 8}
        i = 2
        j = 1
        while i < n:
            if j == k:
                print(i)
            i += 2
            j += 1

    else:
        i = 0
        j = 1
        k = abs((n//2)-k)
        while i < n:
            if j == k:
                print(i+2)
            i += 2
            j += 1

        
    
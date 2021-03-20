#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 17:28:48 2020

@author: yash
"""
import math
# Even-Odd:
n, k = map(int, input().split()) # 10 3
x = (n+1)/2 # 5.5
if x >= k:  # 5.5 >= 3 # True 
    print(2*k-1)
else:
    k = math.ceil(k - x)
    print(2*k)
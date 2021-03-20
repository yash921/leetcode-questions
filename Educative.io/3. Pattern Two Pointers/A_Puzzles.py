#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 16:40:00 2020

@author: yash
"""


n, m = map(int, input().split())
arr = list(map(int, input().split()))
best = float("inf")
arr.sort()
for i in range(m-n+1):
    best = min(best, arr[n+i-1] - arr[i])
print(best)
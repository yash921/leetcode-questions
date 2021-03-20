#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 19:22:30 2020

@author: yash
"""
# Minimum number of Bottles visible when a bottle can be enclosed inside another Bottle1

# Python3 code for the above approach 
def min_visible_bottles(arr, n): 
    m = dict() 
    ans = 0
    for i in range(n): 
        m[arr[i]] = m.get(arr[i], 0) + 1
        ans = max(ans, m[arr[i]]) 
  
    print("Minimum number of", 
          "Visible Bottles are: ", ans) 
n = int(input())
arr = list(map(int, input().strip().split()))
min_visible_bottles(arr,n)
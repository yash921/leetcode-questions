#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 20:19:44 2020

@author: yash
"""

# for _ in range(int(input())):
#     n = int(input())
#     print(len(str)
        
# for _ in range(int(input())):
#     a, b = map(int, input().split())
#     print(a-1, b)
def solve(l, x): 
   
    count = 0    
    for i in range(len(l)):
        if sorted(l) == l:
            break
        if l[i] > x:
            l[i], x = x, l[i]
            count += 1
    if sorted(l) == l:
        return count
    else:
        return -1


for _ in range(int(input())):
    n, x = map(int, input().split())
    l = list(map(int, input().split()))    
+    print(solve(l,x))
        
        
        
    
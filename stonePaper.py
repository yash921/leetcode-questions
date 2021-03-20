#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 16:20:55 2020

@author: yash
"""

lst = list(map(str, input().strip().split()))
scoreA = 0
scoreB = 0
for i in range(len(lst[0])):
    if lst[0][i] == 'R' and lst[1][i] == 'S':
        scoreA += 1
    elif lst[0][i] == 'S' and lst[1][i] == 'R':
        scoreB += 1
    elif lst[0][i] == 'S' and lst[1][i] == 'P':
        scoreA += 1
    elif lst[0][i] == 'P' and lst[1][i] == 'S':
        scoreB += 1
    elif lst[0][i] == 'P' and lst[1][i] == 'R':
        scoreA += 1
    elif lst[0][i] == 'R' and lst[1][i] == 'P':
        scoreB += 1
    
if scoreA > scoreB:
    print("ALYSSA")
elif scoreA < scoreB:
    print("JAMES")
else:
    print("TIE")





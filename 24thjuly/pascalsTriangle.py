#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 16:56:46 2020

@author: yash
"""

def PascalTriangle(num):
    l = []
    
    for i in range(num):
        l.append([0]*(i+1))
    for i in range(num):
        for j in range(i+1):
            if j == 0:
                l[i][j] = 1
            elif i == j:
                l[i][j] = 1
            else:
                l[i][j] = l[i-1][j-1] + l[i-1][j]
    return l

print(PascalTriangle(4))
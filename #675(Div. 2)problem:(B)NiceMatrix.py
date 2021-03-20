#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 14:58:59 2020

@author: yash
"""
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    
    steps = 0
    for i in range(n):
        for j in range(m):
            x = [a[i][j], a[n-i-1][j], a[i][m-j-1], a[n-i-1][m-j-1]]
            x.sort()
            steps += abs(a[i][j] - x[1])
            a[i][j] = x[1]
    print(steps)
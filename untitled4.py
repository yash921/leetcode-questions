#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 13:06:17 2020

@author: yash
"""

for i in range(int(input())):
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append([[int(x) for x in input().split()] for i in range(2)])
    
    check = False
    for i in range(n):
        check |= a[i][0][0] == a[i][1][1]
    check &= m%2 == 0
    print("YES" if check else "NO")
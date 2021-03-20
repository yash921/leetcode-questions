#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 20:33:09 2020

@author: yash
"""

for _ in range(int(input())):
    n = int(input())
    s = input()
    def solve(s):
        l = ['t', 'r', 'y', 'g', 'u', 'b']
        temp = ''
        for i in s:
            if i in l:
                if i == l[0]:
                    temp += i
                    l.remove(l[0])
        if temp == "trygub":
           print(''.join(sorted(s)))    
        else:
            print(s)
    solve(s)           



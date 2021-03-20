#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 09:48:22 2020

@author: yash
"""

a = [0,-5,30212,10]
b = [-10,40,-3,9]
a.extend(b)
target = -8
x = {}
for i in range(len(a)):
    num = a[i]
    potentialSum = (target) - (num)
    if num in x:
        print(a[num],i)
    else:
        x[potentialSum] = i
        
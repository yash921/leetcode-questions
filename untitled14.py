#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 23:13:13 2020

@author: yash
"""
#How to create 1D array??

#Method-1
# N = 20
# arr = [0] * N
# print(arr)

#Method-2
# N = 20
# arr = [0 for i in range(N)]
# print(arr)


#How to create 2D array??

#Method-1
# row, col = (3,3)
# arr = [[0] * col ] * row
# print(arr)

#Method-1
# row, col = (3,3)
# arr =[ [0 for i in range(col)] for j in range(row)]
# print(arr)

for i in range(100):
    n = input()
    if len(n) == 1:
        print(ord(n))     
    else:
        print("invalid character")
        break
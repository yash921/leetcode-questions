#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 11:08:06 2020

@author: yash
"""

n = int(input())
for coin in range(n):
    chanek_count = -1
    coin = int(input())    
    while coin > 0:
        if coin%2 != 0 or coin == 2:
            chanek_count += 1
            coin -= 2
        else:
            chanek_count += 2
            coin -= 1
    print(chanek_count)
                
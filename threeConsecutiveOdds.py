#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 22:27:13 2020

@author: yash
"""

def threeConsecutiveOdds(arr):
    count = 0
    for i in arr:
        if i % 2 != 0:
            count +=1
            if count == 3:
                return True
        else:
            count = 0
    
    
print(threeConsecutiveOdds([823,384,282,984,218,3,127,227,55,266]))
        


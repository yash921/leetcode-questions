#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 14:46:56 2020

@author: yash
"""
# ###Binary Search Approach
# O(n) time | O(1) space
def findThreeLargestNumbers(array):
    threeLargest = [None for i in range(3)] # [None, None, None]
    for num in array:
        updateLargest(threeLargest, num)
    return threeLargest

def updateLargest(threeLargest, num):
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftAndUpdate(threeLargest, num, 2)
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate(threeLargest, num, 1)
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftAndUpdate(threeLargest, num, 0)

def shiftAndUpdate(array, num, indx):
    #[0,1,2]
    #[y,z,num]
    #for i in range(0, 2+1)
    #if i == 1:
        
        
        
    for i in range(indx+1):
          if i == indx:
              array[i] = num
          else:
              array[i] = array[i+1]
            
print(findThreeLargestNumbers([12,3,-3,51312,12,34,121]))
        
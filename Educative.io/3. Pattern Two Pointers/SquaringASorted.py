#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 17:44:08 2020

@author: yash
"""

def SquaringASortedArray(array):
    """
    arr = [-2, -1, 0, 2, 3]
           ^            ^
         left          right
         
    squareArr = [0, 0, 0, 0, 0]
    
    """
    n = len(array)
    squares = [0 for x in range(n)]
    highestSquareIdx = n - 1
    left, right = 0, n - 1
    while left <= right:
        leftSquare = array[left]**2
        rightSquare = array[right]**2
        if leftSquare > rightSquare:
            squares[highestSquareIdx] = leftSquare
            left += 1
        else:
            squares[highestSquareIdx] = rightSquare
            right -= 1
        highestSquareIdx -= 1
    return squares

print(SquaringASortedArray([-3, -1, 0, 1, 2]))
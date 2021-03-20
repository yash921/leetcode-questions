#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 16:34:15 2020

@author: yash
"""

#Binary Search,
# array = [2,3,1,43,5,6,67,112]

def BinarySearch(array, target):
    array.sort()
    leftPointer = 0
    rightPointer = len(array) - 1
    while leftPointer <= rightPointer:
        middle = (leftPointer + rightPointer) // 2
        potentialMiddle = array[middle]
        if potentialMiddle == target:
            return middle
        elif potentialMiddle > target:
            rightPointer = middle - 1
        elif potentialMiddle < target:
            leftPointer = middle + 1
    return -1

print(BinarySearch([2,3,1,43,5,6,67,112],112))
        
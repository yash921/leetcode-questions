#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 13:06:18 2020

@author: yash
"""

def thSum(array,target):
    array.sort()
    diff = float("inf")
    for i in range(len(array)):
        leftPointer = i+1
        rightPointer = len(array)-1
        while leftPointer < rightPointer:
            currentNo = array[i]
            currentSum = currentNo + array[leftPointer] + array[rightPointer]
            current = abs(target - currentSum)
            if current < abs(diff):
                diff = current
                #leftPointer+=1
                #rightPointer-=1
            elif currentSum < target:
                leftPointer+=1
            elif currentSum > target:
                rightPointer-=1
    return target - diff
                
print(thSum([-1,2,1,-4],1
))
        
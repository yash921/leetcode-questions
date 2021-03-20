#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 16:15:10 2020

@author: yash
"""

def TripletSumCloseToTarget(array, target):
    array.sort() #[-2, 0, 1, 2]
    closest = float("inf")
    for i in range(len(array)-2):
        if i > 0 and array[i] == array[i-1]:
            continue
        left = i+1
        right = len(array) - 1
        while left < right:
            currentNum = array[i]
            currentSum = currentNum + array[left] + array[right]
            if currentSum == target:
                closest = 0
                return target - closest
            if abs(target - currentSum) < abs(closest):
                closest  = target - currentSum
            elif currentSum < target:
                left += 1
            else:
                right -= 1
    return target - closest

print(TripletSumCloseToTarget([-2, 0, 1, 2], 2)) 
                
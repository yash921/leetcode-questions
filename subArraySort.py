#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 02:23:40 2020

@author: yash
"""
# 581. Shortest Unsorted Continuous Subarray



#AlgoExpert - subArraySort
# Time = O(n) | Space = O(1)
def sumArraySort(array):
    minOutOfOrder = float("inf")
    maxOutOfOrder = float("-inf")
    
    for i in range(len(array)):
        num = array[i]
        if isOutOfOrder(i, num, array):
            minOutOfOrder =  min(minOutOfOrder, num)
            maxOutOfOrder = max(maxOutOfOrder, num)
    if minOutOfOrder == float("inf"):
        return [-1,-1]
    subArrayLeftIdx = 0
    while minOutOfOrder >= array[subArrayLeftIdx]:
        subArrayLeftIdx += 1
    subArrayRightIdx = len(array) - 1
    while maxOutOfOrder <= array[subArrayRightIdx]:
        subArrayRightIdx -= 1
    return len(array[subArrayLeftIdx:subArrayRightIdx+1])
    
        
def isOutOfOrder(i, num, array):
    if i == 0:
        return num > array[i + 1]
    if i == len(array) - 1:
        return num < array[i - 1]
    return num > array[i + 1] or num < array[i - 1]


print(sumArraySort([2, 6, 4, 8, 10, 9, 15]))
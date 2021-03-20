#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 18:50:59 2020

@author: yash
"""

def QuickSort(array):
    QuickSortHelper(array, 0, len(array) - 1)
    return array

def QuickSortHelper(array, startIdx, endIdx):
    if startIdx >= endIdx:
        return 
    pivotIdx = startIdx
    leftIdx = startIdx + 1
    rightIdx = endIdx
    while rightIdx >= leftIdx:
        if array[leftIdx] >= array[pivotIdx] and array[pivotIdx] >= array[rightIdx]:
            swap(array, leftIdx, rightIdx)
        elif array[pivotIdx] >= array[leftIdx]:
            leftIdx+=1
        elif array[rightIdx] >= array[pivotIdx]:
            rightIdx -= 1
        swap(array, pivotIdx, rightIdx)
        leftsu
            
            
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
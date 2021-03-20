#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 18:42:35 2020

@author: yash
"""

def bubbleSort(array):
    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(len(array)-1-counter):
            if array[i] > array[i+1]:
                swap(i, i+1, array)
                isSorted = False
        counter+=1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
    
print(bubbleSort([31415926535897932384626433832795,
1,
3,
10,
3,
5,]))
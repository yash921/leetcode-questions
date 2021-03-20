#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 18:35:48 2020

@author: yash
"""

# def insertionSort(array):
#     for i in range(1, len(array)):
#         temp = array[i]
#         j = i - 1
#         while temp < array[j] and j >= 0:
#             array[j+1] = array[j]
#             j = j-1
#         array[j+1] = temp
#     return array

def insertionSort(array):
    count = 0
    for i in range(1,len(array)):
        j = i
        while j > 0 and array[j-1] > array[j]:
            swap(array,j,j-1)
            count+=1
            j = j - 1
    return count

def swap(array,i,j):
    array[i],array[j] = array[j],array[i]
    
    
print(insertionSort([9,8,7,6,5,4,3,2,1]))    
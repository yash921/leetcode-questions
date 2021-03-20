#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 11:23:20 2020

@author: yash
"""
# O(N^2) Time | O(1) Space 
# def selectionSort(array):
#     currentIdx = 0
#     while currentIdx < len(array) - 1:
#         smallestIdx = currentIdx
#         for i in range(currentIdx+1, len(array)):
#             if array[smallestIdx] > array[i]:
#                 smallestIdx = i
#         array[currentIdx], array[smallestIdx] = array[smallestIdx], array[currentIdx]
#         currentIdx += 1
#     return array

# print(selectionSort([9,8,7,6,5,4,3,2,1]))
            
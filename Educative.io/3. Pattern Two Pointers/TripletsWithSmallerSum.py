#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 00:36:28 2020

@author: yash
"""
# Time O(N*logN + N^2) which is asymptotically equivalent to O(N^2).
# Space O(N) which is required for sorting if we are not using an in-place sorting algorithm.
# def TripletsWithSmallerSum(array, target):
#     array.sort()
#     counter = 0
#     for i in range(len(array)-2):
#         left = i+1
#         right = len(array)-1
#         currentNum = array[i]
#         while left < right:
#             currentNum = array[i]
#             currentSum = currentNum + array[left] + array[right]
#             if currentSum < target:   #[-1, 0, 2, 3]
#                 counter += (right - left)
#                 left += 1
#             else:
#                 right -= 1               
#     return counter

            
# print(TripletsWithSmallerSum([-1, 0, 2, 3], 3))   


###############################################################################

def TripletsWithSmallerSum(array, target):
    triplets = []
    array.sort()
    for i in range(len(array)-2):
        left = i+1
        right = len(array)-1
        currentNum = array[i]
        while left < right:
            currentNum = array[i]
            currentSum = currentNum + array[left] + array[right]
            if currentSum < target:   #[-1, 0, 2, 3]
                for i in range(right, left, -1):
                    triplets.append([currentNum, array[left], array[i]])
                left += 1
            else:
                right -= 1               
    return triplets
         

print(TripletsWithSmallerSum([-1, 0, 2, 3], 3))
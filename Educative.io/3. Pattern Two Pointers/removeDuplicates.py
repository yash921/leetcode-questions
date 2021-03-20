#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 20:05:57 2020

@author: yash
"""
# Time O(n) | Space O(1)
# def removeDuplicates(nums):
#     """
#                                nums : [0,0,1,1,1,2,2,3,3,4]
#     last index to overwrite-on (j) :     ^
#     Iterator                   (i):      ^
#     Final nums array             :   [0,1,2,3,4,2,2,3,3,4]
#     Return Ans                  :             5
#     """
#     next_non_duplicate = 1
#     i = 1 #next
#     while i < len(nums):
#         if nums[next_non_duplicate - 1] != nums[i]:
#             nums[next_non_duplicate] = nums[i]
#             next_non_duplicate += 1
#         i += 1
#     return next_non_duplicate
            

# print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

###############################################################################

def removeKey(array, key):
    nextElement = 0
    for i in range(len(array)):
        if array[i] != key:
            array[nextElement] = array[i]
            nextElement += 1
    return nextElement
            
print(removeKey([3, 2, 3, 6, 3, 10, 9, 3], 3))
            





















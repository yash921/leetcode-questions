#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 09:45:15 2020

@author: yash
"""

class Solution:
    #Solution-1
    def isMonotonic(self, array: List[int]) -> bool:
        isNonDecreasing = True
        isNonIncreasing = True
        for i in range(1,len(array)):
            if array[i] > array[i-1]:
                isNonIncreasing = False
            if array[i] < array[i-1]:
                isNonDecreasing = False
        return isNonDecreasing or isNonIncreasing
    
#Solution-2
#         direction1 = float("inf")
#         direction2 = float("inf")
#         direction3 = float("inf")
#         i = 0
#         while i < len(array) - 1:
#             while i < len(array) - 2  and array[i] == array[i+1]:
#                 direction1 = "neu"
#                 i+=1
#             if array[i] < array[i+1]:
#                 direction2 = "inc"
#             elif array[i] > array[i+1]:
#                 direction3 = "dec"
#             i+=1
        
#         if direction1 and type(direction2) == str and type(direction3) == str :
#             return False    
        
#         elif direction1 or direction2:
#             return True
        
#         elif direction1 or direction3:
#             return True
        
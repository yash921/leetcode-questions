#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 13:40:32 2020

@author: yash
"""
# def sumOfTwo(num1, num2, target):
#     for i in range(len(num1)):
#         needed_value = target - num1[i]
#         for j in range(len(num2)):
#             if num2[j] == needed_value:
#                 return True
#     return False

def sumOfTwo(list1, list2, target):
    d = []
    for i in list1:
        needed_value = target - i
        d.append(needed_value)
    for j in list2:
        if j in d:
            return True
    
    return False
        

print(sumOfTwo([9,3,1,4],[0,1,4,5],9))
                 













# def firstNotRepeatingCharacter(s):
#     d = {}
#     for i in s:
#         if i in d:
#             d[i]+=1
#         else:
#             d[i] = 1
#     for i in d:
#         if d[i] == 1:
#             return i
#     return '_'

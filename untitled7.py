#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 13:46:09 2020

@author: yash
"""

#Augest 


#######################---> Week-1 <---#############################
#Day - 1:
# def detectCapitalUse(word):
#     count = 0
#     for i in range(len(word)):
#         if word[i].isupper():
#             count+=1
#     return count == len(word) or count == 0 or count == 1 and word[0].isupper()
    

# print(detectCapitalUse("u"))
            
#Day - 2:
#Solution-1
# class MyHashSet:

#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.array = [None for _ in range(1000000)]
        

#     def add(self, key: int) -> None:
#         if not self.contains(key):
#             self.array[key] = True
        

#     def remove(self, key: int) -> None:
#         if self.contains(key):
#             self.array[key] = None
        

#     def contains(self, key: int) -> bool:
#         """
#         Returns true if this set contains the specified element
#         """
#         return self.array[key]

#Solution-2

#Day - 3:
#Solution
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = s.lower()
#         ans = ''
#         for char in s:
#             if char in 'abcdefghijklmnopqrstuvwxyz0123456789':
#                 ans = ans + char
#         new = ans[::-1]
#         if ans == new:
#             return True
#         else:
#             return False


    


                    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 17:38:07 2020

@author: yash
"""

# #Solution - 1 - Reverse the string
# # Time O(n^2) | Space O(n)
# def palindronCheck(string):
#     new_str = ""
#     for i in reversed(range(len(string))):
#         new_str += string[i]
#     return new_str == string

# print(palindronCheck('abab'))

###############################################################

# #Solution - 2 - Using a list
# # Time O(n) | Space O(n)
# def palindronCheckB(string):
#     new_list = []
#     for i in reversed(range(len(string))):
#         new_list.append(string[i])
#     return "".join(new_list) == string

# print(palindronCheck('ababa'))

###############################################################

#Solution - 3 - tail recursion
# Time O(n) | Space O(n)
# def palindronCheck(string, i=0):
#     j = len(string) - 1 - i
#     # return True if i >= j else string[i] == string[j] and palindronCheck(string, i+1)
    
#     if i >= j:
#         return True
#     elif string[i] != string[j]:
#         return False
#     else:
#         return palindronCheck(string, i + 1)
    
# print(palindronCheck('abasdsd'))

###################################################################

#Solution - 4 - Using Pointers
# Time O(n) | Space O(1)
def palindronCheck(string):
    i = 0
    j = len(string) - 1
    while i < j:
        if string[i] != string[j]:
            return False
        i+=1
        j-=1
    return True

print(palindronCheck('aba'))























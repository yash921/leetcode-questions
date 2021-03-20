#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 18:20:23 2020

@author: yash
"""

# # O(M + N) Time | Space O(N + M)
# def ComparingStringsContainingBackspaces(str1, str2):
#     def Build(string):
#         ans = []
#         for c in string:
#             if c != '#':
#                 ans.append(c)
#             elif ans:
#                 ans.pop()
#         return ''.join(ans)
#     return Build(str1) == Build(str2)

########################################################

# O(N) Time | Space O(1)
def ComparingStringsContainingBackspaces(str1, str2):

    index1 = len(str1) - 1
    index2 = len(str2) - 1
    while index1 >= 0 or index2 >= 0:
        i1 = get_next_valid_char_index(str1, index1) # "xy#z"
        i2 = get_next_valid_char_index(str2, index2) # "xzz#"
        
        if i1 < 0 and i2 < 0:
            return True
        if i1 < 0 or i2 < 0:
            return False
        if str1[i1] != str2[i2]:
            return False
        
        index1 = i1 - 1
        index2 = i2 - 1
    return True
        

def get_next_valid_char_index(string, index):
    backspace_count = 0
    while index >= 0:
        if string[index] == '#':
            backspace_count += 1
        elif backspace_count > 0:
            backspace_count -= 1
        else:
            break
        
        index -= 1
    return index
    
                
            


print(ComparingStringsContainingBackspaces("ab##", "c#d#"))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 09:50:47 2020

@author: yash
"""

def PermutationInAString(string, pattern):
    window_start, matched = 0, 0
    char_frequency = {}
    for i,char in enumerate(pattern):
        if char not in char_frequency:
            char_frequency[char] = 0
        char_frequency[char] += 1
    
    for window_end in range(len(string)):
        right_char = string[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1
        
        if matched == len(pattern):
            return True
        
        if window_end >= len(pattern) - 1:
            left_char = string[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1
    return False
    
print(PermutationInAString("oidbcaf", "abc" ))
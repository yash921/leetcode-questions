#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 17 01:08:05 2020

@author: yash
"""

def SmallestWindowcontainingSubstring(string, pattern):
    window_start, matched, substr_start = 0, 0, 0
    min_length = len(string)
    char_frequency = {}
    for i, char in enumerate(pattern):
        if char not in char_frequency:
            char_frequency[char] = 0
        char_frequency[char] += 1
    
    for window_end in range(len(string)):
        right_char = string[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] >= 0:
                matched += 1
        
        while matched == len(pattern):
            if min_length > window_end - window_start + 1:
                min_length = window_end - window_start + 1
                substr_start = window_start
                
            left_char = string[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1
        
    if min_length > len(string):
            return ""
    return string[substr_start: substr_start + min_length]
                
            
print(SmallestWindowcontainingSubstring("aabdec","abc"))       
    
    
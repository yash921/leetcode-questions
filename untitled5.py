#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 19:10:45 2020

@author: yash
"""

def Longest_Substring_with_K_Distinct_Characters(string, k):
    window_start = 0
    max_length = 0
    char_frequency = {}
    for window_end in range(len(string)):
        right_char = string[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1
        
        while len(char_frequency) > k:
            left_char = string[window_end]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1
        
        max_length = max(max_length, window_end - window_start + 1)
        
    return max_length
        
        
            
    
print(Longest_Substring_with_K_Distinct_Characters("araaaaaaaaci", 3))
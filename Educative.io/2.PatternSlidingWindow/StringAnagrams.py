#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 14:28:53 2020

@author: yash
"""

def stringAnagrams(string, pattern):
    if len(pattern) == len(string):
        return "".join(sorted(string)) == "".join(sorted(pattern))
    window_start = 0
    matched = 0
    result = []
    char_frequency = {}
    for i, char in enumerate(pattern):
        if char not in char_frequency:
            char_frequency[char] = 0
        char_frequency[char] += 1
        
    for window_end in range(len(string)):
        right_char = string[window_end]
        
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1
        print(matched)
        
        if matched == len(char_frequency):
            result.append(window_start)
        
        if window_end >= len(pattern) - 1:
            left_char = string[window_start]
            window_start += 1
            
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1
    return result
                    
            
   
print(stringAnagrams("paqpqp", "qpq" ))



    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
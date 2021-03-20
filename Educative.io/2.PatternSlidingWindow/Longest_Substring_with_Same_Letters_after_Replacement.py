#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 18:11:24 2020

@author: yash
"""

# Problem Statement #

# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

# Example 1:

# Input: String="aabccbb", k=2
# Output: 5
# Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

# Example 2:

# Input: String="abbcb", k=1
# Output: 4
# Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".

# Example 3:

# Input: String="abccde", k=1
# Output: 3
# Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".


#O(n) Time | O(26) --> O(1) Space
def Longest_Substring_with_Same_Letters_after_Replacement(string, k):
    window_start = 0
    max_length = 0
    max_repeat_letter_count = 0
    frequency_map = {}
    for window_end in range(len(string)):
        char = string[window_end]
        if char not in frequency_map:
            frequency_map[char] = 0
        frequency_map[char] += 1
        max_repeat_letter_count = max(max_repeat_letter_count, frequency_map[char])
        
        
        if (window_end - window_start + 1 - max_repeat_letter_count) > k:
            left_char = string[window_start]
            frequency_map[left_char] -= 1
            window_start += 1
        
        max_length = max(max_length, window_end - window_start + 1)
    return max_length

print(Longest_Substring_with_Same_Letters_after_Replacement("ABAB",2))
    
    
# Time Complexity #
# The time complexity of the above algorithm will be O(N) where ‘N’ is the number of letters in the input string.


# Space Complexity #
# As we are expecting only the lower case letters in the input string, we can conclude that the space complexity will be O(26), to store each letter’s frequency in the HashMap, which is asymptotically equal to O(1).

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
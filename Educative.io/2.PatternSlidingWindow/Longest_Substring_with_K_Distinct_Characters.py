#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 19:10:45 2020

@author: yash
"""
# Problem Statement #

# Given a string, find the length of the longest substring in it with no more than K distinct characters.

# Example 1:

# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".

# Example 2:

# Input: String="araaci", K=1
# Output: 2
# Explanation: The longest substring with no more than '1' distinct characters is "aa".

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

# Time Complexity #

# The time complexity of the above algorithm will be O(N) where ‘N’ is the number of characters in the input string. The outer for loop runs for all characters and the inner while loop processes each character only once, therefore the time complexity of the algorithm will be O(N+N) which is asymptotically equivalent to O(N).
# Space Complexity #

# The space complexity of the algorithm is O(K), as we will be storing a maximum of ‘K+1’ characters in the HashMap.

        
print(Longest_Substring_with_K_Distinct_Characters("araaaaaaaaci", 3))
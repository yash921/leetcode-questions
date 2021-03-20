#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 23:47:27 2020

@author: yash
"""

#  def checkPermutation(string, pattern):
#     map_frequency = {}
#     counter = 0
#     for i in range(len(pattern)):
#         if pattern[i] not in map_frequency:
#             map_frequency[pattern[i]] = 1
#         map_frequency[pattern[i]] += 1
        
        

# print(checkPermutation("bbbca","abc"))

# def maxSlidingWindow(array, k):
#     avgList = []
#     largest = 0
#     windowStart = 0
#     for windowEnd in range(len(array)):
#         if windowEnd - windowStart + > k: 
#             avgList.append(largest)
#             windowStart += 1
#         largest = max(largest, array[windowEnd])
#     return avgList
    

# print(maxSlidingWindow([1,-1], 1))

# def SmallestSubarraywithAgivensum(array, givenSum):
#     window_start = 0
#     smallest_length = float("inf")
#     window_sum = 0
#     for window_end in range(len(array)):
#         window_sum += array[window_end]
        
#         while window_sum >= givenSum:
#             smallest_length = min(smallest_length, window_end - window_start + 1)
#             window_sum -= array[window_start]37
#             window_start += 1
#     if smallest_length == float("inf"):
#         return -1
#     else:
#         return smallest_length

# print(SmallestSubarraywithAgivensum([84,-37,32,40,95], 167))
            

# def LongestSubstringwithKDistinctCharacters(string, k):
#     window_start = 0
#     longest_subString = 0
#     char_frequency = {}
#     for window_end in range(len(string)):
#         char = string[window_end]
#         if char not in char_frequency:
#             char_frequency[char] = 0
#         char_frequency[char] += 1
        
#         while len(char_frequency) > k:
#             left_char = 
        
        
#         longest_subString = max(longest_subString, window_end - window_start + 1)


# print(longest_subString)

# LongestSubstringwithKDistinctCharacters("araaci", 2)


# def LongestSubstringwithKDistinctCharacters(string, k):
#     window_start = 0
#     max_length = 0
#     char_frequency = {}
#     for window_end in range(len(string)):
#         char = string[window_end]
#         if char not in char_frequency:
#             char_frequency[char] = 0
#         char_frequency[char] += 1
        
#         while len(char_frequency) > k:
#             left_char = string[window_start]
#             char_frequency[left_char] -= 1
#             if char_frequency[left_char] == 0:
#                 del char_frequency[left_char]
#             window_start += 1
#         max_length = max(max_length, window_end - window_start + 1)
#     return max_length
# print(LongestSubstringwithKDistinctCharacters("araaci", 2))
# # 


# def fruitsIntoBaskets(array):
#     char_hash_map = {}
#     window_start = 0
#     max_length = 0
#     for window_end in range(len(array)):
#         char = array[window_end]
#         if char not in char_hash_map:
#             char_hash_map[char] = 0
#         char_hash_map[char] += 1
#         # {"A": 2, "B": 1, "C": 2}
#         while len(char_hash_map) > 2:
#             left_char = array[window_start]
#             char_hash_map[left_char] -= 1
#             if char_hash_map[left_char] == 0:
#                 del char_hash_map[left_char]
#             window_start += 1
#         max_length = max(max_length, window_end - window_start + 1)
#     return max_length

# print(fruitsIntoBaskets(['A', 'B', 'C', 'B', 'B', 'C']))
            
# def NoRepeatSubstring(string):
#     window_start = 0
#     max_length = 0
#     char_frequency = {}
#     for window_end in range(len(string)):
#         right_char = string[window_end]
#         if right_char in char_frequency:
#             window_start = max(window_start, char_frequency[right_char] + 1)
#         char_frequency[right_char] = window_end
#         max_length = max(max_length, window_end - window_start + 1)
#     return max_length

# def LongestSubstringwithSameLettersafterReplacement(string, k):
#     window_start = 0
#     max_Repeat_Letter_Count = 0
#     char_frequency = {}
#     for window_end in range(len(string)):


def PermutationInAString(string, pattern):
    window_start = 0
    patternCount = 0
    pattern_frequency = {}
    for i,char in enumerate(pattern):
        if char not in pattern_frequency:
            pattern_frequency[char] = 0
        pattern_frequency[char] += 1
    
    for window_end in range(len(string)):
        left_char = string[window_end]
        if left_char in pattern_frequency:
            window_start = window_end
        
    print(patternCount1, patternCount2)


print(PermutationInAString("oidbcaf", "abc"))









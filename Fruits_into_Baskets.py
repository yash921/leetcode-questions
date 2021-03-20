#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 17:28:51 2020

@author: yash
"""

# Example 1:

# Input: Fruit=['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

# Example 2:

# Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
# Output: 5
# Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
# This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']

def fruits_Into_Baskets(Fruits):
    window_start = 0
    max_length = 0
    fruit_frequency = {}
    for window_end in range(len(Fruits)):
        fruit = Fruits[window_end]
        if fruit not in fruit_frequency:
            fruit_frequency[fruit] = 0
        fruit_frequency[fruit] += 1
        
        
        while len(fruit_frequency) > 2:
            left_char = Fruits[window_start]
            fruit_frequency[left_char] -= 1
            if fruit_frequency[left_char] == 0:
                del fruit_frequency[left_char]
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length

# Time Complexity #

# The time complexity of the above algorithm will be O(N) where ‘N’ is the number of characters in the input array. The outer for loop runs for all characters and the inner while loop processes each character only once, therefore the time complexity of the algorithm will be O(N+N) which is asymptotically equivalent to O(N).
# Space Complexity #

# The algorithm runs in constant space O(1) as there can be a maximum of three types of fruits stored in the frequency map.
    
    
# print(fruits_Into_Baskets(['A', 'B', 'C', 'B', 'B', 'C']))
print(fruits_Into_Baskets([1,0,2,0,1]))

        
        
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 00:44:39 2020

@author: yash
"""
# 242. Valid Anagram

# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:

# Input: s = "rat", t = "car"
# Output: false

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # return sorted(s) == sorted(t)
        if len(s) != len(t):
            return False
        elif len(s) == 0:
            return True
        
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        
        for char in alphabet:
            if s.count(char) != t.count(char):
                return False
            
        return True
        
        

        
        
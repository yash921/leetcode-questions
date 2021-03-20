#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 20:24:18 2020

@author: yash
"""
# Solution - 1:
#O(n) Time | O(n) Space
class Solution:
    def isValid(self, strings: str) -> bool:
        openingBracket = "({["
        closingBracket = ")}]"
        matchingBracket = {")":"(", "}":"{", "]":"["}
        stack = []
        for char in strings:
            if char in openingBracket:
                stack.append(char)
            elif char in closingBracket:
                if len(stack) == 0:
                    return False
                elif stack[-1] == matchingBracket[char]:
                    stack.pop()
                else:
                    return False
        return not stack
    
# Solution - 2:
#O(n + extra time) | O(1) Space
class Solution:
    def isValid(self, s: str) -> bool:
        while("()" in s or "{}" in s or "[]" in s):
            s = s.replace("()", "")
            s = s.replace("{}", "")
            s = s.replace("[]", "")
        if s != "":
            return False
        else:
            return True
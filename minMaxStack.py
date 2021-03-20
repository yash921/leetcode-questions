#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 15:43:12 2020

@author: yash
"""

class MinMaxStack:
    def __init__(self):
        self.minMaxStack = []
        self.stack = []
    
    # O(1) time | O(1) space
    def peek(self):
        return self.stack[len(self.stack) - 1]
    
    # O(1) time | O(1) space
    def pop(self):
        if not self.stack:
            return "Enpty List"
        self.minMaxStack.pop()
        return self.stack.pop()
    
    # O(1) time | O(1) space
    def push(self, number):
        newMinMax = {"min": number, "max": number}
        if len(self.minMaxStack):
            lastMinMax = self.minMaxStack[len(self.minMaxStack) - 1]
            newMinMax["min"] = min(lastMinMax["min"], number)
            newMinMax["max"] = max(lastMinMax["max"], number)
        self.minMaxStack.append(newMinMax)
        self.stack.append(number)
        
    # O(1) time | O(1) space
    def getMin(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["min"]
    
    # O(1) time | O(1) space
    def getMax(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["max"]
    
ans = MinMaxStack()
print(ans.pop())
    
    
            
        
        
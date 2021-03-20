#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 23:46:39 2020

@author: yash
"""

# We have a collection of stones, each stone has a positive integer weight.

# Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

#     If x == y, both stones are totally destroyed;
#     If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.

# At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

# Example 1:

# Input: [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.


#############Solution###########

#Solution - 1
class Solution:
    def lastStoneWeight(self, stones):
        for i in range(len(stones) - 1):
            stones.sort()
            stones.append(stones.pop() - stones.pop())
        return stones[0]
    
#----------------------------------------#

#Solution-2
class Solution:
    def lastStoneWeight(self, stones):
        stones = [-i for i in stones]
        myheap = MinHeap(stones)
    
        while len(stones)>1:
            first = abs(myheap.remove())
            second = abs(myheap.remove())
            if first != second:
                myheap.insert(-abs(first - second))
                    
            # this compact return statement way is great ^_^
        return abs(stones[0]) if len(stones) else 0

class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)
        
        
    # O(n) time | O(1) space
    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array
    
    
    
    # O(log(n)) time | O(1) space
    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                break
            
            
    # O(log(n)) time | O(1) space
    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2
            
            
    # O(1) time | O(1) space
    def peek(self):
        return self.heap[0]
    
    
    # O(log(n)) time | O(1) space
    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove
    
    
    # O(log(n)) time | O(1) space
    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)
        
        
    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]

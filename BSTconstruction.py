#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 18:50:47 2020

@author: yash
"""
import pygame


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
        
        
    #  Average: O(log(n)) time | O(1) space
    # Worst: O(n) time | O(1) space
    def insert(self, value):
        currentNode = self
        while True:
            if value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = BST(value)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = BST(value)
                    break
                else:
                    currentNode = currentNode.right
        return self
    
    
    # Average: O(log(n)) time | O(1) space
    # Worst: O(n) time | O(1) space
    def contains(self, value):
        currentNode = self
        while currentNode is not None:
            if value < currentNode.value:
                currentNode = currentNode.left
            elif value > currentNode.value:
                currentNode = currentNode.right
            else:
                return True
        return False
    
  
    
  
def findClosestValue(tree, target):
    return findClosestValueInBstHelper(tree, target, float("inf"))
    
def findClosestValueInBstHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, closest)
    else:
        return closest
    
    
myTree = BST(1)
myTree.left = BST(2)
myTree.right = BST(3)
# myTree.insert(2)
# myTree.insert(3)
print(findClosestValue(myTree,4))



#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 15:09:48 2020

@author: yash
"""

class BinaryTree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
        
        
def branchSum(root):
    sums = []
    calculateBranchSums(root, 0, sums)
    return sums

def calculateBranchSums(node, runningSum, sums):
    if node is None:
        return 
    newRunningSum = runningSum + node.value
    if node.left is None and node.right is None:
        sums.append(newRunningSum)
        return
    calculateBranchSums(node.left, newRunningSum, sums)
    calculateBranchSums(node.right, newRunningSum, sums)
    
myTree = BinaryTree(1)
myTree.left = BinaryTree(2)
myTree.right = BinaryTree(3)
myTree.left.left = BinaryTree(4)
myTree.right.right = BinaryTree(7)
myTree.left.right = BinaryTree(5)
myTree.right.left = BinaryTree(6)
myTree.left.left.left = BinaryTree(8)
myTree.left.left.right = BinaryTree(9)
myTree.left.right.left = BinaryTree(10)
print(branchSum(myTree))
    
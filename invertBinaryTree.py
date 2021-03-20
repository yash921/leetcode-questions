#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 10:48:50 2020

@author: yash
"""

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
#Solution-1-Recursive Way 
#Time = O(n) | Space = O(n)
# # class InvertedTree:
# def InvertBinaryTree(root):
#     queue = [root]
#     while len(queue):
#         current = queue.pop(0)
#         if current is None:
#             continue
#         swapLeftAndRight(current)
#         queue.append(current.left)
#         queue.append(current.right)
#     return root
            
# def swapLeftAndRight(node):
#         node.left, node.right = node.right, node.left

###################

#Solution-2-By Swaping
#Time = O(n) | space = O(d)
def invertBinaryTree(root):
    if root is None:
        return
    swapLeftAndRight(root)
    invertBinaryTree(root.left)
    invertBinaryTree(root.right)
    
def swapLeftAndRight(node):
    node.left, node.right = node.right, node.left
    
    
    
    
    
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
print(invertBinaryTree(myTree))
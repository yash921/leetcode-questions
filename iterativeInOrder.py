#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 21:12:06 2020

@author: yash
"""
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None

def iterativeInOrderTraversal(tree, callback):
    previousNode = None
    currentNode = tree
    while currentNode is not None:
        if previousNode is None or previousNode == currentNode.parent:
            if currentNode.left is not None:
                nextNode = currentNode.left
            else:
                callback.append(currentNode.value)
                nextNode = currentNode.right if currentNode.right is not None else currentNode.parent
        elif previousNode == currentNode.left:
    
            callback.append(currentNode.value)
            nextNode = currentNode.right if currentNode.right is not None else currentNode.parent
        else:
            nextNode = currentNode.parent
        previousNode = currentNode
        currentNode = nextNode
    return callback
        
myTree = BinaryTree(1)
myTree.left = BinaryTree(2)
print(iterativeInOrderTraversal(myTree, []))
        

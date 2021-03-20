#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 19:34:58 2020

@author: yash
"""

class ClosestValueInBST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#Solution - Recursive
# Average: O(log(n)) time | O(log(n)) space
# Worst: O(n) time | O(n) space  
# def findClosestValue(tree, target):
#     return findClosestValuehelper(tree, target, float("inf"))
    
# def findClosestValuehelper(tree, target, closest):
#     if tree is None:
#         return closest
#     if abs(target - closest) > abs(target - tree.value):
#         closest = tree.value
#     elif target < tree.value:
#         findClosestValuehelper(tree.left, target, closest)
#     elif target > tree.value:
#         findClosestValuehelper(tree.right, target, closest)
#     else:
#         return closest
        
#---------------------------------------#

#Solutaion - Iterative
# Average: O(log(n)) time | O(1) space
# Worst: O(n) time | O(1) space  
def findClosestValue(tree, target):
    return findClosestValuehelper(tree, target, float("inf"))

def findClosestValuehelper(tree, target, closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        elif target < currentNode.value:
            currentNode = currentNode.left
        elif target > currentNode.value:
            currentNode = currentNode.right
        else:
            break
    return closest
        


   
myTree = ClosestValueInBST(10)
myTree.right = ClosestValueInBST(15)
myTree.left = ClosestValueInBST(5)
myTree.left.left = ClosestValueInBST(2)
myTree.left.right = ClosestValueInBST(5)
myTree.left.left.left = ClosestValueInBST(1)
myTree.right.left = ClosestValueInBST(13)
myTree.right.rightf = ClosestValueInBST(22)
myTree.right.left.left = ClosestValueInBST(14)



print(findClosestValue(myTree, 12))
        
    
    
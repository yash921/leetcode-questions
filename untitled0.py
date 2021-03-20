#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 16:42:49 2020

@author: yash
"""

def flattenBinaryTree(root):
    inOrderNodes = getNodeInorder(root, [])
    p

def getNodeInorder(node, array):
    if node is not None:
        getNodeInorder(node.left)
        array.append(node)
        getNodeInorder(node.right)
    return array
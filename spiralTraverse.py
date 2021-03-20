#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 09:34:14 2020

@author: yash
"""
#Solution-1-Iteratively-(T=O(n), S=O(n))
# def spiralTraverse(array):
#     result = []
#     startRow, endRow = 0, len(array) - 1
#     startCol, endCol = 0, len(array[0]) - 1
    
#     while startRow <= endRow and startCol <= endCol:
        
#         for col in range(startCol, endCol+1):
#             result.append(array[startRow][col])
            
#         for row in range(startRow+1, endRow+1):
#             result.append(array[row][endCol])
        
#         for col in reversed(range(startCol, endCol)):
#             result.append(array[endRow][col])
            
#         for row in reversed(range(startRow+1, endRow)):
#             result.append(array[row][startCol])
            
#         startRow+=1
#         endRow-+1
#         startCol+=1
#         endCol-=1
#     return result

###############################################################################

# #Solution-2-Recursively(T=O(n), S=O(n))
# def spiralTraverse(array):
#     result = []
#     spiralFill(array, 0, len(array) - 1, 0, len(array[0]) - 1, result)
#     return result

# def spiralFill(array, startRow, endRow, startCol, endCol, result):
#     if startRow > endRow or startCol > endCol:
#         return
#     for col in range(startCol, endCol + 1):
#         result.append(array[startRow][col])
#     for row in range(startRow + 1, endRow + 1):
#         result.append(array[row][endCol])
#     for col in reversed(range(startCol, endCol)):
#         if startRow == endRow:
#             break
#         result.append(array[endRow][col])
#     for row in reversed(range(startRow + 1, endRow)):
#         if startCol == endCol:
#             break
#         result.append(array[row][startCol])
#     spiralFill(array, startRow + 1, endRow - 1, startCol + 1, endCol - 1, result)
    
###****Best Solution****###############
def spiralTraverse(matrix):
    return matrix and [*matrix.pop(0)] + spiralTraverse([*zip(*matrix)][::-1])
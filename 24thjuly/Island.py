#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 13:19:54 2020

@author: yash
"""
# class Solution:
#     """
#     :type grid: List[List[str]]
#     :rtype: int
#     """
#     def numIsisland(self,grid):
#         if grid is None and len(grid) == 0:
#             return 0
#         count = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[i])):
#                 if grid[i][j] == '1':
#                     count+= 1
#                     self.dfsHelperFunc(grid,i,j)
#         return count
    
#     def dfsHelperFunc(self,grid,i,j):
#         if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == '0':
#             return
#         grid[i][j] = '0'
#         self.dfsHelperFunc(grid,i-1,j)
#         self.dfsHelperFunc(grid,i,j-1)
#         self.dfsHelperFunc(grid,i+1,j)
#         self.dfsHelperFunc(grid,i,j+1)




#Solution-2
















grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
] 
       
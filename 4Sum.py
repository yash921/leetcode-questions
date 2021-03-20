#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 12:53:48 2020

@author: yash
"""

# Copyright © 2020 AlgoExpert, LLC. All rights reserved.
# Average: O(n^2) time | O(n^2) space
# Worst: O(n^3) time | O(n^2) space
# def fourNumberSum(array, targetSum):
#     allPairSums = {}
#     quadruplets = []
#     for i in range(1, len(array) - 1):
#         for j in range(i + 1, len(array)):
#             currentSum = array[i] + array[j]
#             difference = targetSum - currentSum
#             if difference in allPairSums:
#                 for pair in allPairSums[difference]:
#                     quadruplets.append(pair + [array[i], array[j]])
#         for k in range(0, i):
#             currentSum = array[i] + array[k]
#             if currentSum not in allPairSums:
#                 allPairSums[currentSum] = [[array[k], array[i]]]
#             else:
#                 allPairSums[currentSum].append([array[k], array[i]])
      # res = list(set(tuple(sorted(sub)) for sub in quadruplets))
#     return res


def fourNumberSum(array, target):
    m = []
    for i in range(0,len(array)-3):
        for j in range(i+1,len(array)-2):
            for k in range(j+1, len(array)-1):
                for l in range(k+1,len(array)):
                    if array[i]+array[j]+array[k]+array[l] == target:
                        m.append([array[i],array[j],array[k],array[l]])
    return m

print(fourNumberSum([10, 2, 3, 4, 5, 9, 7, 8], 23)) 


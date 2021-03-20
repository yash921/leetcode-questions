#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 11:04:40 2020

@author: yash
"""
#Solution - 1
#Time - O(n) | Space - O(1)
def validSubsequence(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1
    return seqIdx == len(sequence)


#Solution - 2
#Time - O(n) | Space - O(1)
# def validSubsequence(array, sequence):
#     seqIdx = 0
#     for value in array:
#         if seqIdx == len(sequence):
#             break
#         if value == sequence[seqIdx]:
#             seqIdx += 1
#     return seqIdx == len(sequence)



print(validSubsequence([21,3,1,4,53,1,-3], [3,4,1]))
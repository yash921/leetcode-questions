#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 12:23:25 2020

@author: yash
"""

# def twoSmallestDifference(arrayOne, arrayTwo):
#     arrayOne.sort()
#     arrayTwo.sort()
#     idxOne = 0
#     idxTwo = 0
#     smallestDiff = float("inf")
#     currentDiff = float("inf")
#     smallestPair = []
#     while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
#         firstNum = arrayOne[idxOne]
#         secondNum = arrayTwo[idxTwo]
#         if firstNum < secondNum:
#             currentDiff = secondNum - firstNum
#             idxOne+=1
#         elif firstNum > secondNum:
#             currentDiff = firstNum - secondNum
#             idxTwo+=1
#         else:
#             return [firstNum, secondNum]
#         if smallestDiff > currentDiff:
#             smallestDiff = currentDiff
#             smallestPair = [firstNum, secondNum]
#     return smallestPair


def twoSmallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0
    smallestDiff = float("inf")
    currentDiff = float("inf")
    smallestPair = []
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]
        if firstNum < secondNum:
            currentDiff = secondNum - firstNum
            idxOne+=1
        elif firstNum > secondNum:
            currentDiff = firstNum - secondNum
            idxTwo+=1
        else:
            return [firstNum, secondNum]
        if smallestDiff > currentDiff:
            smallestDiff = currentDiff
            smallestPair = [firstNum, secondNum]
    return smallestPair

print(twoSmallestDifference([12,10], [2,15,20]))
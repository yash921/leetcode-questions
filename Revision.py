#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 13:14:22 2020

@author: yash
"""

# def ThreeSum(array, target):
#     array.sort()
#     tripLets = []
#     for i in range(len(array) - 2):
#         leftPointer = i + 1
#         rightPointer = len(array) - 1
#         while leftPointer < rightPointer:
#             currentNo = array[i]
#             currentSum = currentNo + array[leftPointer] + array[rightPointer]
#             if currentSum == target:
#                 tripLets.append([currentNo, array[leftPointer], array[rightPointer]])
#                 leftPointer += 1
#                 rightPointer -= 1
#             elif currentSum < target:
#                 leftPointer += 1
#             else:
#                 rightPointer -= 1
#     return tripLets

# print(ThreeSum([8,6,9,2,1,10,7], 17))



# def insertion_Solution_1(array):
#     for i in range(1, len(array)):
#         temp = array[i]
#         j = i - 1
#         while temp < array[j] and j >= 0:
#             array[j + 1] = array[j]
#             j = j - 1
#         array[j + 1] = temp
#     return array
# print(insertion([29, 10, 14, 37, 13]))


# def insertion_Solution_2(array):
# #     for i in range(1, len(array)):
# #         while i > 0 and array[i] < array[i - 1]:
# #             swap(i, i-1, array)
# #             i = i - 1
# #     return array
            
# # def swap(i, j, array):
# #     array[i], array[j] = array[j], array[i]
    
# # print(insertion_Solution_2([29, 10, 14, 37, 13]))

# #O(nlogn) Time | O(nlogn) Space
# def mergeSort(array):
#     if len(array) == 1:
#         return array
#     middle = len(array) // 2
#     leftArray = array[:middle]
#     rightArray = array[middle:]
#     return mergeSortHelperFunc(mergeSort(leftArray), mergeSort(rightArray))

# def mergeSortHelperFunc(leftHalf, rightHalf):
#     SortedArray = [None] *(len(leftHalf) + len(rightHalf))
#     i = j = k = 0
#     while i < len(leftHalf) and j < len(rightHalf):
#         if leftHalf[i] < rightHalf[j]:
#             SortedArray[k] = leftHalf[i]
#             i += 1
#         else:
#             SortedArray[k] = rightHalf[j]
#             j += 1
#         k += 1
#     while i < len(leftHalf):
#         SortedArray[k] = leftHalf[i]
#         i += 1
#         k += 1
#     while j < len(rightHalf):
#         SortedArray[k] = rightHalf[j]
#         j += 1
#         k += 1
# #     return SortedArray

# # print(mergeSort([9,8,7,6,5,4,3,2,1]))

# def mergeSort(array):
#     if len(array) == 1:
#         return array
#     middle = len(array) // 2
#     leftArray = array[:middle]
#     rightArray = array[middle:]
#     return mergeArrayHelperFunction(mergeSort(leftArray), mergeSort(rightArray))

# def mergeArrayHelperFunction(leftHalf, rightHalf):
#     SortedArray = [None] * (len(leftHalf) + len(rightHalf))
#     i = j = k = 0
#     while i < len(leftHalf) and j < len(rightHalf):
#         if leftHalf[i] < rightHalf[j]:
#             SortedArray[k] = leftHalf[i]
#             i += 1
#         else:
#             SortedArray[k] = rightHalf[j]
#             j += 1
#         k += 1
        
#     while i < len(leftHalf):
#         SortedArray[k] = leftHalf[i]
#         i += 1
#         k += 1
    
#     while j < len(rightHalf):
#         SortedArray[k] = rightHalf[j]
#         j += 1
#         k += 1
#     return SortedArray
        
# print(mergeSort([9,8,7,6,5,4,3,2,1]))

###########Bubble sort##################
# def bubbleSort(array):
#     isSorted = False
#     counter = 0
#     while not isSorted:
#         isSorted = True
#         for i in range(len(array) - 1 - counter):
#             if array[i] > array[i+1]:
#                 array[i], array[i+1] = array[i+1], array[i]
#                 isSorted = False
#         counter += 1
            
#     return array

# print(bubbleSort([9,8,7,6,5,4,3,2,1]))
                

# def bubbleSort(array):
#     isSorted = False
#     counter = 0
#     while not isSorted:
#         isSorted = True
#         for i in range(len(array)-1-counter):
#             if array[i] > array[i+1]:
#                 array[i], array[i+1] = array[i+1], array[i]
#                 isSorted = False
#         counter += 1
#     return array

# print(bubbleSort([9,8,7,6,5,4,3,2,1]))



























































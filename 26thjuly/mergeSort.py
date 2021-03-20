# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Tue Jul 28 17:06:51 2020

# @author: yash
# """

# # def mergeSort(nums):
# #     if len(nums) == 1:
# #         return nums
# #     middle = len(nums) // 2
# #     leftHalf = nums[:middle]
# #     rightHalf = nums[middle:]
# #     return mergeSortedArrays(mergeSort(leftHalf), mergeSort(rightHalf))

# # def mergeSortedArrays(leftHalf, rightHalf):
# #     SortedArray = [] * (len(leftHalf) + len(rightHalf))
# #     i = j = k = 0
# #     while i < len(leftHalf) and j < len(rightHalf):
# #         if leftHalf[i] <= rightHalf[j]:
# #             SortedArray[k] = leftHalf[i]
# #             i+=1
# #         else:
# #             SortedArray[k] = rightHalf[j]
# #             j+=1
# #         k+=1
# #     while i < len(leftHalf):
# #         SortedArray[k] = leftHalf[i]
# #         i+=1
# #         k+=1
# #     while j < len(rightHalf):
# #         SortedArray[k] = rightHalf[j]
# #         j+=1
# #         k+=1
        
# # Copyright © 2020 AlgoExpert, LLC. All rights reserved.
# # Best: O(nlog(n)) time | O(nlog(n)) space
# # Average: O(nlog(n)) time | O(nlog(n)) space
# # Worst: O(nlog(n)) time | O(nlog(n)) space
# def mergeSort(array):
#     if len(array) == 1:
#         return array
#     middleIdx = len(array) // 2
#     leftHalf = array[:middleIdx]
#     rightHalf = array[middleIdx:]
#     return mergeSortedArrays(mergeSort(leftHalf), mergeSort(rightHalf))
# def mergeSortedArrays(leftHalf, rightHalf):
#     sortedArray = [None] * (len(leftHalf) + len(rightHalf))
#     k = i = j = 0
#     while i < len(leftHalf) and j < len(rightHalf):
#         if leftHalf[i] <= rightHalf[j]:        
#             sortedArray[k] = leftHalf[i]
#             i += 1
#         else:
#             sortedArray[k] = rightHalf[j]
#             j += 1
#         k += 1
#     while i < len(leftHalf):
#         sortedArray[k] = leftHalf[i]
#         i += 1
#         k += 1
#     while j < len(rightHalf):
#         sortedArray[k] = rightHalf[j]
#         j += 1
#         k += 1
#     return sortedArray

# print(mergeSort([5,1,1,2,0,0]))
        
    
        
class Solution:
    def sortArray(self, nums):
        if len(nums) == 1:
            return nums
        middle = len(nums) // 2
        leftHalf = nums[:middle]
        rightHalf = nums[middle:]
        return self.mergeSortedArrays(self.mergeSort(leftHalf), self.mergeSort(rightHalf))
    def mergeSortedArrays(leftHalf, rightHalf):
        SortedArray = [None] * (len(leftHalf) + len(rightHalf))
        i = j = k = 0
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] <= rightHalf[j]:
                SortedArray[k] = leftHalf[i]
                i+=1
            else:
                SortedArray[k] = rightHalf[j]
                j+=1
            k+=1
        while i < len(leftHalf):
            SortedArray[k] = leftHalf[i]
            i+=1
            k+=1
        while j < len(rightHalf):
            SortedArray[k] = rightHalf[j]
            j+=1
            k+=1
        return SortedArray
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
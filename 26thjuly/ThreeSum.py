#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 12:54:54 2020

@author: yash
"""
def ThreeSum(array,target):
    array.sort()
    #triplets = set()
    triplets = []
    for i in range(len(array) - 2):
        leftPointer = i + 1
        rightPointer = len(array) - 1
        while leftPointer < rightPointer:
            currentNo = array[i]
            currentSum = currentNo + array[leftPointer] + array[rightPointer]
            if currentSum == target:
                triplets.append([currentNo, array[leftPointer], array[rightPointer]])
                #triplets.add( tuple(sorted([currentNo, nums[leftPointer], nums[rightPointer]])))
                leftPointer+=1
                rightPointer-=1
            elif currentSum < target:
                leftPointer+=1
            elif currentSum > target:
                rightPointer-=1
   
print(ThreeSum([-1, 0, 1, 2,-1,-4],0))

















# def twoSum(nums, target):
#     nums.sort()
#     leftPointer = 0
#     rightPointer = len(nums) - 1
#     while leftPointer < rightPointer:
#         potentialMatch = nums[leftPointer] + nums[rightPointer]
#         if potentialMatch == target:
#             return [leftPointer,rightPointer]
#         elif potentialMatch < target:
#             leftPointer+=1
          
#         else:
#             rightPointer-=1
            
#     return -1
    
# def twoSum(nums, target):
#     d = {}
#     for i in range(len(nums)):
#         num = nums[i]
#         potentialSum = target - num
#         if num in d:
#             return [d[num],i]
#         else:
#             d[potentialSum] = i


        
    

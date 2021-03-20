#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 15:26:34 2020

@author: yash
"""

def threeSum(nums):
    nums.sort()
    triplets = []
    target = 0
    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        leftPointer = i + 1
        rightPointer = len(nums) - 1
        while leftPointer < rightPointer:
            currentNo = nums[i]
            currentSum = currentNo + nums[leftPointer] + nums[rightPointer]
            if currentSum == target:
                triplets.append([currentNo, nums[leftPointer], nums[rightPointer]])
                leftPointer+=1
                rightPointer-=1
                while leftPointer < rightPointer and nums[leftPointer] == nums[leftPointer - 1]:
                    leftPointer += 1
                while leftPointer < rightPointer and nums[rightPointer] == nums[rightPointer + 1]:
                    rightPointer -= 1
            elif currentSum < target:
                leftPointer+=1
            elif currentSum > target:
                rightPointer-=1
    return triplets

print(threeSum([-1,0,1,2,-1,-4]))
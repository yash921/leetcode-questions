#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 17:02:10 2020

@author: yash
"""

# 287. Find the Duplicate Number

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one duplicate number in nums, return this duplicate number.

# Follow-ups:

#     How can we prove that at least one duplicate number must exist in nums? 
#     Can you solve the problem without modifying the array nums?
#     Can you solve the problem using only constant, O(1) extra space?
#     Can you solve the problem with runtime complexity less than O(n2)?

 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2

# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3


################Solutions###########

#Solution - 1:

# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         # nums.sort()
#         # for i in range(1, len(nums)):
#         #     if nums[i] == nums[i-1]:
#         #         return nums[i]



#Solution - 2:
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
          # d = {}
          # for i in nums:
          #     if i in d:
          #         return i
          #     else:
          #         d[i] = True
        
 
        
#Solution - 3:
# class Solution:
#     def findDuplicate(self, nums):
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return num
#             seen.add(num)


def containsNearbyAlmostDuplicate(nums, k, t):
    d = {}
    for idx in range(0, len(nums)):
        if nums[idx] in d and k >= (idx - d[nums[idx]]):
            print(nums[idx])
            print(nums[d[nums[idx]]])
            print(nums[idx] - d[nums[idx]])
            return True
        else:
            d[nums[idx]] = idx
    return False

print(containsNearbyAlmostDuplicate([1,2,3,1], 3,0))
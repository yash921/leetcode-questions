#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 20:15:42 2020

@author: yash
# """
# Problem - 198. House Robber
# #You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police

#Solution - 1
#Time = O(N) | Space = O(N)
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         if len(nums) == 1:
#             return nums[0]
#         maxSums = nums[:]
#         maxSums[1] = max(nums[0], nums[1])
#         for i in range(2, len(nums)):
#             maxSums[i] = max(maxSums[i-1], maxSums[i-2]+nums[i])
#         return maxSums[-1]
        
###########################################################################################

#Solution - 2
#Time = O(N) | Space = O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        second = nums[0]
        first = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            current = max(first, second+nums[i])
            second = first
            first = current
        return first
            
        
        
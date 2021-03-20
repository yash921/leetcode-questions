#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 20:18:00 2020

@author: yash
"""
#Problem - 213. House Robber II
# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

# Example 1:

# Input: [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
#              because they are adjacent houses.




#Solution - 1:
# #Time = O(N) | Space = O(N)
# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         if not nums:
#             return 0
#         if len(nums) == 1:
#             return nums[0]
#         if len(nums) == 2:
#             return max(nums[0], nums[1])
#         def House_Robber(nums):
#             maxSums = [0]*len(nums)
#             maxSums[0] = nums[0]
#             maxSums[1] = max(nums[0], nums[1])
#             for i in range(2, len(nums)):
#                 maxSums[i] = max(maxSums[i-1], maxSums[i-2]+nums[i])
#             return max(maxSums[-2], maxSums[-1])
        
#         return max(House_Robber(nums[1:]), House_Robber(nums[:-1]))
            

#Solution - 2:    
#Time = O(N) | Space = O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        def House_Robber(nums):
            second = nums[0]
            first = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                current = max(first, second+nums[i])
                second = first
                first = current
            return first
        
        return max(House_Robber(nums[1:]), House_Robber(nums[:-1]))
            
        
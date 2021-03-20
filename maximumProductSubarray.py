#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 12:02:24 2020

@author: yash
"""
# 152. Maximum Product Subarray

#Solution - 1

#Time - O(N) | Space = O(N)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) < 1: return 0
        
        dp_max = [0]*len(nums)
        dp_min = [0]*len(nums)
        
        dp_max[0] = dp_min[0] = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > 0:
                dp_max[i] = max(dp_max[i-1]*nums[i], nums[i])
                dp_min[i] = min(dp_min[i-1]*nums[i], nums[i])
            else:
                dp_max[i] = max(dp_min[i-1]*nums[i], nums[i])
                dp_min[i] = min(dp_max[i-1]*nums[i], nums[i])
        return max(dp_max)

    
#Solution - 2

#Time = O(N) | Space = O(1)
#Solution - 1 
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) < 1: return 0
        
        _max = cur_max = cur_min = nums[0]
        
        for n in nums[1:]:
            temp = cur_max
            cur_max = max(cur_max*n, cur_min*n ,n)
            cur_min = min(temp*n, cur_min*n, n)
            _max = max(_max, cur_max)
            
        return _max
           
        
        
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 10:00:52 2020

@author: yash
"""
#121. Best Time to Buy and Sell Stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        ans = 0 
        mini = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < mini:
                mini = prices[i]
            else:
                ans = max(ans, prices[i] - mini)
        return ans
        
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 10:55:54 2020

@author: yash
"""

#122. Best Time to Buy and Sell Stock II


# Example 1:

# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
#              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3
class Solution:
    def BuySellStocks(self,prices):
        if not prices:
            return 0
        maxProfit = 0
        mini = prices[0]
        for i in range(1, len(prices)):
            if mini > prices[i]:
                mini = prices[i]
            else:
                maxProfit+= (prices[i] - mini)
                mini = prices[i]
        return maxProfit

profit = Solution()
print(profit.BuySellStocks([7,1,5,3,6,4]))

print(profit)
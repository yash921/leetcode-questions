#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 13:05:52 2020

@author: yash
"""

# arr = [1,11,3,0,15,5,2,4,10,7,12,6]



#Solution - 1 [By Using Sorting]


# Time = O(nlog(n)) | Space = O(1)
# class Solution:
#     def LongestConsecutiveSequence(self, array):
#         if not array:
#             return 0
#         if len(array) == 1:
#             return 1
#         array.sort()
#         longestRange = 0
#         count = 0
#         for i in range(len(array)):
#             if array[i] == array[i-1]+1:
#                 count += 1
#             else:
#                 longestRange = max(longestRange, count)
#                 count = 1
#         return max(longestRange, count)
    
# ans = Solution()
# print(ans.LongestConsecutiveSequence([1,3,5,2]
# ))


#Solution - 2 [Using hashTable]

#Time = O(n) | Space = O(1)
class Solution:
    def largestRange(self, array):
        bestRange = []
        longestLength = 0
        nums = {}
        for num in array:
            nums[num] = True
        for num in nums:
            if not nums[num]:
                continue
            nums[num] = False
            currentLength = 1
            left = num - 1
            right = num + 1
            while left in nums:
                nums[left] = False
                currentLength += 1
                left -= 1
            while right in nums:
                nums[right] = False
                currentLength += 1
                right += 1
            if currentLength > longestLength:
                longestLength = currentLength
                bestRange = [left+1, right-1]
    
        return bestRange  
    
ans = Solution()
print(ans.largestRange([1,11,3,0,15,5,2,4,10,7,12,6]
))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    



        
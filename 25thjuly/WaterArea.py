# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Sat Jul 25 13:02:09 2020

# @author: yash
# """
# def waterArea(heights):
    # """
    # Time = O(N) | Space = O(N)
    # """
    # maxs = [0 for x in heights]
    # leftmaxs = [0 for x in heights]
    # rightmaxs = [0 for x in heights]
    # leftMax = 0
    # for i in range(len(heights)):
    #     height = heights[i]  #1
    #     leftmaxs[i] = leftMax
    #     leftMax = max(leftMax, height)
    # rightMax = 0
    # for i in reversed(range(len(heights))):
    #     height = heights[i]
    #     rightmaxs[i] = rightMax
    #     rightMax = max(rightMax, height)
    # for i in range(len(heights)):
    #     height = heights[i]
    #     minHeight = min(leftmaxs[i],rightmaxs[i])
    #     if height < minHeight:
    #         maxs[i] = minHeight - height
    #     else:
    #         maxs[i] = 0
    # return sum(maxs)



# ############################################

# # O(n) time | O(n) space
def waterArea(heights):
    maxes = [0 for x in heights]
    leftMax = 0
    for i in range(len(heights)):
        height = heights[i]
        maxes[i] = leftMax
        leftMax = max(leftMax, height)
    rightMax = 0
    for i in reversed(range(len(heights))):
        height = heights[i]
        minHeight = min(rightMax, maxes[i])
    if height < minHeight:
        maxes[i] = minHeight - height
    else:
         maxes[i] = 0
         rightMax = max(rightMax, height)
    return sum(maxes)
print(waterArea([1,8,6,2,5,4,8,3,7]))
            
    
    
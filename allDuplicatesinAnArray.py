#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 01:36:47 2020

@author: yash
"""
def allDuplicatesinAnArray(nums):
    output_list = []
    for i in range(len(nums)):
        index = abs(nums[i]) - 1
        if nums[index] < 0:
            output_list.append(index + 1)
        else:
            nums[index] = -nums[index]
    return output_list

print(allDuplicatesinAnArray([4,3,2,7,8,2,3,1]))

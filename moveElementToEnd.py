#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 18:56:30 2020

@author: yash
"""
#Leetcode Problem - 283. Move Zeroes

#Solution - Best Solution
def moveElementToEnd(array, toMove):
    i = 0
    j = len(array) - 1
    while i < j:
        while i < j and array[j] == toMove:
            j -= 1
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
        i+=1 
        
    return array
print(moveElementToEnd([2,1,2,2,3,4,2,2,2],2))


    
#My Solution    
    # l = []
    # for _ in array:
    #     if _ == value:
    #         count = array.count(_)
    #     else:
    #         l.append(_)
    # for i in range(count):
    #     l.append(value)
    # return l

# def moveEnd(array, value):
#     if value in array:
#         count = array.count(value)
#     for i in range(count):
#             array.remove(value)
#     for i in range(count):
#         array.append(value)
#     print(array)
#print(moveEnd([0,1,3,12],0))
        
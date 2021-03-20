#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 22:46:39 2020

@author: yash
"""


# l = list(map(str, input().split()))
# help = 'abcdefghijklmnopqrstuvwxyz'
# count = 0
# for i in l:
#     if i in help:
#         help = help.replace(i, "")
#         count += 1
# print(count)
# letters = {i for i in input() if i.isalpha()}
# print(len(letters))

###########################################
# n = int(input())
# if len(set(input().split()[1:] + input().split()[1:])) == n:
#     print('I become the guy.')
# else:
#     print('Oh, my keyboard!')

#########################################

n, k = map(int, input().split())
if k > n//2:
    for i in range(n):
        if k == i + 1:
            print(2*(i+1))
        else:
            print(2*(i+1w2))
    
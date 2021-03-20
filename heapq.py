#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 22:37:19 2020

@author: yash
"""

# def isPalindrome(x):
#     stri = str(x)
#     reserverpal = ""
#     if stri[:] == "0":
#         return 
#     else:
#         for i in reversed(range(len(stri))):
#             reserverpal+=stri[i]
#             reserverpal.strip("0")
            
#     return int(reserverpal)
# n = int(input())
# l = []
# for i in range(n):
#     l.append(int(input()))

# for i in l:
#     print(isPalindrome(i))




def lapindrome(st):
    middle = len(st) // 2
    d_left = {}
    d_right = {}
    if len(st) % 2 == 0:
        for i in st[:middle]:
            if i in d_left:
                d_left[i]+=1
            else:
                d_left[i]=1
                
        for j in st[middle:]:
            if j in d_right:
                d_right[j]+=1
            else:
                d_right[j]=1
    else:
        for i in st[:middle]:
            if i in d_left:
                d_left[i]+=1
            else:
                d_left[i]=1
                
        for j in st[middle+1:]:
            if j in d_right:
                d_right[j]+=1
            else:
                d_right[j]=1
        
    if d_left == d_right:
        print("YES")
    else:
        print("NO")

        
n = int(input())
l = []
for i in range(n):
    l.append(input())

for i in l:
    lapindrome(i)   

    











#import heapq

# l = []

# heapq.heappush(l , 1)
# heapq.heappush(l , 2)
# heapq.heappush(l , 3)
# heapq.heappush(l , 4)
# heapq.heappop(l)
# print(l)
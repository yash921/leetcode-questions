#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 22:10:59 2020

@author: yash
"""

# def longestPalindromSubstring(string):
#     currentLongest = [0, 1]   #babad
#     for i in range(1, len(string)):
#         odd = getLongestPalindromFrom(string, i-1, i+1)
#         even = getLongestPalindromFrom(string, i-1, i)
#         longest = max(odd, even, key= lambda x: x[1] - x[0])
#         currentLongest = max(longest, currentLongest, key= lambda x: x[1] - x[0 ])
#     return string[currentLongest[0]: currentLongest[1]]

# def getLongestPalindromFrom(string, leftIdx, rightIdx):
#     while leftIdx >= 0 and rightIdx < len(string):
#         if string[leftIdx] != string[rightIdx]:
#             break
#         leftIdx -= 1
#         rightIdx += 1
#     return [leftIdx+1, rightIdx]

# print(longestPalindromSubstring("asxxyyxxfdf"))
        
        
# a = 1
# if a:
#     print("q")



def PrintBothArrays(a):
    n = len(a)
    if len(a) < 3:
        return 0
    v1, v2 = [], [];    
    mpp = dict.fromkeys(a, 0);  
    for i in range(n) :  
        mpp[a[i]] += 1;  
        if (mpp[a[i]] == 1) : 
            v1.append(a[i]);    
        elif (mpp[a[i]] == 2) :  
            v2.append(a[i]);  
        else :  
            print("Not possible");  
            return;   
    v1.sort();  
    v2.sort(reverse = True);
    if len(v1) == 0 or len(v2) == 0:
        return 0
    v2.append(v1[0])
    i = 0
    while i < len(v1)-1:
        if v1[i] < v1[i+1]:
            pass
        else:
            return 0
        i += 1
    j = 0
    while j < len(v2)-1:
        if v2[j] > v2[j+1]:
            pass
        else:
            return 0
        j += 1
    return 1
    
# Driver code  
if __name__ == "__main__" :
    a = [4, 0, 5, 1, 2, 3]  
    print(PrintBothArrays(a))










 
  











    
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 09:34:30 2020

@author: yash
"""
##########Determine whether an integer is a palindrome.##################################
###########An integer is a palindrome when it reads the same backward as forward.########
def isPalindrome(x):
    stri = str(x)
    reserverpal = ""
    if stri[0] == "-":
        return False
    else:
        for i in reversed(range(len(stri))):
            reserverpal+=stri[i]
    return stri == reserverpal

print(isPalindrome(-121))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 17:16:43 2020

@author: yash
"""
##166. Fraction to Recurring Decimal
# Example 1:

# Input: numerator = 1, denominator = 2
#Output: "0.5"

# Example 2:

# Input: numerator = 2, denominator = 1
# Output: "2"

# Example 3:

# Input: numerator = 2, denominator = 3
# Output: "0.(6)"

###LeetCode Solution###

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if denominator == 0:
            return 'Undefined'
        if numerator == 0:
            return "0"
        neg = False
        if numerator*denominator < 0:
            neg = True
        if numerator % denominator == 0:
            return str(numerator//denominator)
        
        numerator = abs(numerator)
        denominator = abs(denominator)
        
        output = ""
        if neg == True:
            output+="-"
        output+=str(numerator // denominator)
        output+="."
        
        num_q = []
        while True:
            rem = numerator % denominator
            numerator = rem*10
            if rem == 0:
                for element in num_q:
                    output+=str(element[-1])
                break
            q = numerator // denominator
            if [numerator, q] not in num_q:
                num_q.append([numerator, q])
            elif [numerator, q] in num_q:
                indx = num_q.index([numerator, q])
                for element in num_q[:indx]:
                    output+=str(element[-1])
                output+="("
                for element in num_q[indx:]:
                    output+=str(element[-1])
                output+=")"
                break
        return output
                    
            
#######################################


def repeating_decimal(num, deno):
    if deno == 0:
        return 'Undefined'
    if num == 0:
        return '0'
    neg = False
    if num*deno < 0:
        neg = True
    if num % deno == 0:
        return str(num//deno)
    
    numerator = abs(num)
    denominator = abs(deno)
    output = ""
    if neg == True:
        output+="-"
    output+=str(numerator // denominator)
    output+="."
    
    num_q = []
    while True:
        rem = numerator % denominator
        if rem == 0:
            for elemet in num_q:
                output+=str(elemet[-1])
            break
        numerator = rem*10
        q = numerator // denominator
        
        if [numerator, q] not in num_q:
            num_q.append([numerator, q])
        elif [numerator, q] in num_q:
            indx = num_q.index([numerator, q])
            for elemet in num_q[:indx]:
                output+=str(elemet[-1])
                
            output+="("
            for elemet in num_q[indx:]:
                output+=str(elemet[-1])
            output+=")"
            break
    return output
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 14:57:15 2020

@author: yash
"""
# Count the number of prime numbers less than a non-negative number, n.

# Example:

# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7

class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        prime = [True for i in range(n)]
        p = 2
        while (p*p <= n):
            if prime[p] == True:
                for i in range(p*2, n, p):
                    prime[i] = False
            p+=1
        prime[0] = False
        prime[1] = False
        count = 0
        for p in range(n):
            if prime[p]:
                count+=1
        return count
        
print(countPrimes(3))
               
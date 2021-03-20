#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 16:45:41 2020

@author: yash
"""
#Solution-1-->using Recursion
def getNthfib(n):
    """
    Time = O(2^n) | Space = O(n) --> Because of Function call stack
    """
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return getNthfib(n-1) + getNthfib(n-2)
    
<------------------------------------------------->


#Solution-2-->Usning memoize hash tables
def getNthfib(n, memoize):
    """
    Time = O(n) | Space = O(n)
    """
    if n in memoize:
        return memoize[n]
    else:
        ans = getNthfib(n-1, memoize) + getNthfib(n-2, memoize)
        ans = memoize[n]
        return ans
        
memoize = {1:0, 2:1}
#example = fib_efficient(6, d)

<------------------------------------------------>



#Solution-3-->Using iteration

def getNthfib(n):
    lasttwo = [0,1]
    counter = 3
    while counter <= n:
        nextfib = lasttwo[0] + lasttwo[1]
        lasttwo[0] = lasttwo[1]
        lasttwo[1] = nextfib
        counter+=1
    return lasttwo[1] if n > 1 else lasttwo[0]

print(getNthfib(4))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


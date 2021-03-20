#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 16:54:54 2020

@author: yash
"""

def mutate_string(string, position, character):
    l = list(s)
    l[position] = character
    y = ''
    y = y.join(l)
    return y

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
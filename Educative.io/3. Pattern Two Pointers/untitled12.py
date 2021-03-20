#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 00:19:43 2020

@author: yash
"""

def StringChallenge(str1,str2="asdada"):
  hash_map = {}
  for i, char in enumerate(str1):
    if char not in hash_map:
      hash_map[char] = 0
    hash_map[char] += 1

  for i in str2:
    if i in hash_map:
      str2.count(i) == hash_map[i]
    else:
      return "false"
  return "true"

# keep this function call here 
print(StringChallenge(input()))
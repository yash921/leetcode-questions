#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 23:09:52 2020

@author: yash
"""
import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
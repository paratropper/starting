# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 17:08:24 2019

@author: HP
"""
str1 = input("enter string")
dict1 = {}

str2 = set(str1)
counter = 0

for i in str1:
    if i in dict1:
        dict1[i] = dict1[i]+1
    else:
        dict1[i]=1
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 17:15:29 2019

@author: HP
"""

dict1 =  {"a" : 2, "b" : 15, "c" : 13}
sum1 = 0
for i in dict1.keys():
    if 13<=dict1[i]<=19:
        continue
    if dict1[i]<=13 and dict1[i]>=19:
        print(dict1[i])
        if dict1[i] == 16 or dict1[i] == 15:
            sum1 = sum1 + i
    print(sum1)
        
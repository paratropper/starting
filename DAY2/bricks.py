# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 17:23:05 2019

@author: HP
"""

brick1 = int(input("enter small brick value"))
brick2 = int(input("enter big brick value"))
target = int(input("enter target value"))
if target%5 >brick1:
    print(False)
else:
    if brick1 + brick2*5>=target:
        print("true")
    else:
        print("false")
            
    

# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 17:41:03 2019

@author: HP
"""

lst = []
while True :
    a = input()
    if not a:
        break
    lst.append(int(a))
    lst.reverse()
    print(lst)
    
    

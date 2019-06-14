# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:46:32 2019

@author: HP
"""

list1 = []
while True:
    user_input = input("Enter values >")
    
    if not user_input:
        break
    list1.append(user_input)
   
    
tuple1 = tuple(list1)   
print(list1)
print(tuple1)

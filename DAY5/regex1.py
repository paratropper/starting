# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:30:07 2019

@author: HP
"""
import re

str1 = (input("enter the string>"))
re1 = re.match(r'[+-.]?\d+\.\d{1,}',str1)
if re1:
    print("true")
else:
    print("false")

        

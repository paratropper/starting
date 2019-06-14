# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 18:01:55 2019

@author: HP
"""

alphabet = input("enter the name>")
digit1 = 0
letter1 = 0
str1 = 'qwertyuiopasdfghjklzxcvbnm'
for i in alphabet:
    if i in str1:
        letter1 = letter1 + 1
    else:
            digit1 = digit1 + 1

print(letter1)
print(digit1)
            
        
    
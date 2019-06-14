# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:13:12 2019

@author: HP
"""

file = open('absentee.txt', mode = 'wt')

while True:
    user_input = input("enter the data max 25>") 
    file.write(user_input)
    if not user_input:
        break
file.close()

file = open('absentee.txt', mode = 'rt')
a=file.read()
print(a.split(","))
file.close()

        
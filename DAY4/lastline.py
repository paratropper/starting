# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:54:48 2019

@author: HP
"""

#file = open("user_file.txt", mode = 'wt')

with open('user_file.txt', mode='rt') as file :
    file_content = file.readlines()[-1]
    print(file_content)
file.close()
    

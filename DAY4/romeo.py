# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:33:52 2019

@author: HP
"""

character = {}
file = open("romeo.txt", mode = "rt")

with open ("romeo.txt", 'rt'):
    for line in file:
        file.readline().split(" ")
        
    for word in file:
        if word in character.keys():
            character[word] = character[word] + 1
        else:
            character[word]=1


print(character)
file.close()
        
    
        
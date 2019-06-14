# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:04:18 2019

@author: HP
"""
list_of_integers = input("enter values separated by commas").split(",")
total = 0

for index in range( len( list_of_integers ) ):
    if (list_of_integers[index] == 13 or list_of_integers[index-1] == 13):
        continue
    total += 1

print (total)
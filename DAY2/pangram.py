# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:43:49 2019

@author: HP
"""

 
import string 

def ispangram(str): 
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	for char in alphabet: 
		if char not in str.lower(): 
			return False

	return True
str = input("enter string")
if(ispangram(str) == True): 
	print("pangram") 
else: 
	print("not pangram") 

   

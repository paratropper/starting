# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:51:23 2019

@author: HP
"""
file1 = open('new.txt', mode='rt')
file2 = open('new1.txt', mode='wt')
with open ("new.txt", "rt") as file1 :
  with open ("new1.txt", "wt") as file2 :
    for line in file1 :
      file2.write(line)
 
          
      
      
      
      
with open ("new.txt", "rt"):
  with open ("new.txt", "wt"):
    for line in file :
      file.write ( line)
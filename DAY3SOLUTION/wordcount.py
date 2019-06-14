# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:48:53 2019

@author: HP
"""
"""
file = open("name.txt", mode = 'wt')

while True:
    user_input = input("enter the data> ")
    file.write(user_input)
    if not user_input:
        break
 """   
#file.close()

file = open("name.txt", mode = 'rt') 
text = file.read()   

print("characters")
print (len(text))

file_content =text.split()
print("words")
print(len(file_content))

num_lines = 0

file.close()
with open ("name.txt", "rt") as file :
    for line in file:
        num_lines = num_lines + 1

print("numbers of lines")        
print(num_lines)

print("unique words")
print(len(set(file_content)))


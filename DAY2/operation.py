# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 18:14:24 2019

@author: HP
"""
def add():
    sum = 0
    for sum in number:
        sum += number
        return sum
def multiply():
    multiply = 1
    for multiply in number:
        multiply *= number
        return multiply
def largest():
    for i in number:
        if(number[i]>number[i + 1]):
            return("largest")
        else:
           break
def smallest():
    for i in number:
        if number[i + 1] < number[i]:
            return("largest")
        else:
            break
def sort():
    sort_value = number.sort()
    return sort_value
def duplicate_removed():
    for i in number:
        if(number[i] == number[i+1]):
             number.pop(i)
             
    return number 







while True:
    number = input("enter number of values")
    if not number:
         break
    
             
             
                     
                     
                         
           
   
         
        
   
       
       
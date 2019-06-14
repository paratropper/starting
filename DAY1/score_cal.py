# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 17:29:36 2019

@author: HP
"""
assignment = 3            #no of assignment
A1 = float(input("enter assignment one marks"))
A2 = float(input("enter assignment two marks"))
A3 = float(input("enter assignment three marks"))
exams = 2                  #no of exams
E1 = float(input("enter exam one marks"))
E2 = float(input("enter exam two marks"))
score = 100              #max score
weighted_score = (A1 + A2 + A3) * 0.1 + (E1 + E2) * 0.35
print(weighted_score)


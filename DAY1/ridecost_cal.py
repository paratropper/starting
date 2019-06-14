# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 17:20:09 2019

@author: HP
"""

total_distance = 80
diesel_price_per_litre = 80
average = 18
total_fuel_consume = float(total_distance / average)
total_cost = total_fuel_consume * diesel_price_per_litre
print(total_cost)
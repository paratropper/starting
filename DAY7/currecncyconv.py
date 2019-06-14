# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 16:50:16 2019

@author: HP
"""
import json
import requests

url =  "https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=a6dcca552cf5de34bc18"
print("url")
response = requests.get(url)
jsondata = response.json()
print (type(jsondata))
print("current USD to INR price is:")
print(jsondata)



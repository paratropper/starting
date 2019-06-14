# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:28:02 2019

@author: HP
"""

import json
import requests

Host = "https://enxmbftb0ypy.x.pipedream.net"

data = {"phone number":"9982290143","name":"ramesh","college_name":"babu_lal_commerce_college","branch":"chokidar"}

headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post_method():
    response = requests.post(Host,data,headers)
    return response

print ( post_method().text )

def get_method():
    response = requests.get("https://enxmbftb0ypy.x.pipedream.net/get?phonenumber=9982290143&name=ramesh&college_name=babu_lal_commerce_college&branch=chokidar")
    return response

print (get_method().text)
print(data)

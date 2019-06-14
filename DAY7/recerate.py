# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 17:11:48 2019

@author: HP
"""

import json
import requests

Host = "https://enxmbftb0ypy.x.pipedream.net"

data = {"firstname":"donNo1","language":"tapori","work":"bhaigiri"}

headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post_method():
    response = requests.post(Host,data,headers)
    return response

print ( post_method().text )
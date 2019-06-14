# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:26:07 2019

@author: HP
"""

import re
list1 = []
while True:
    user_input = input("enter card details")
    if not user_input:
        break
    else:
        list1.append(user_input)

for item in list1:
  re1 = re.findall(r'[456]([0-9]{15}|\d{3\-(\d{4}\-){2}\d{4})',item)
  res1 = re.search(r'(\d)\1{3,}',item.replace("-",""))
  if re1 and not res1:
      print("valid card")
      print(item)
  else:
      print("no")
          






# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:01:25 2019

@author: HP
"""

import re
list1 = ['lara@hackerrank.com','brian-23@hackerrank.com','britts_54@hackerrank.com','#raghu@gmail.com']
list2 = []
for item in list1:
    re2 = re.findall(r'^[a-z0-9\_\-]+@[\w]+\.[a-z]{2,4}$' , item)
    
    if re2:
        
        list2.append(item)
    
    else:
        print("")

list2=sorted(list2)
print(list2)
    
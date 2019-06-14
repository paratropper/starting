# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 15:46:35 2019

@author: HP
"""

from bs4 import BeautifulSoup  
import requests 

url = " https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
source = requests.get(url).text

soup = BeautifulSoup(source,"lxml")
right_table=soup.find('table', class_='table')

A=[]
B=[]
C=[]
D=[]

for row in right_table.findAll('tr'):
    cells = row.findAll('td')
 
    
    if len(cells) == 5:
        A.append(cells[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        
from collections import OrderedDict

col_name = ["serial no","team name","weighted marks","points"]
col_data = OrderedDict(zip(col_name,[A,B,C,D]))       

import pandas as pd
df = pd.DataFrame(col_data) 
df.to_csv("former.csv")
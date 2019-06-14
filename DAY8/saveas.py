# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 16:48:13 2019

@author: HP
"""

import mysql.connector

conn = mysql.connector.connect(user='user_12345', password='user@123',
                              host='db4free.net', database = 'database_123')
c = conn.cursor()
import pandas as pd
from selenium import webdriver

url = "https://bidplus.gem.gov.in/bidlists"

driver = webdriver.Chrome("chromedriver.exe")
driver.get(url) 
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
H=[]

for i in range(1,11):
    r1=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a').text
    A.append(r1)
    r2=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span').text
    B.append(r2)
    r3=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/span').text
    C.append(r3)
    r4=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[2]').text
    D.append(r4)
    r5=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text[:11]
    E.append(r5)
    r6=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text[12:20]
    F.append(r6)
    r7=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text[:11]
    G.append(r7)
    r8=driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text[12:20]
    H.append(r8)

c.execute ("""CREATE TABLE bid(
          bId TEXT ,
          items  TEXT,
          Quantity_required INTEGER,
          department_name_and_address TEXT,
          start_time TEXT,
          start_date TEXT,
          end_time TEXT,
          end_date TEXT
          )""")

for i in range(0,10):
    c.execute("INSERT INTO bid VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(A[i],B[i],C[i],D[i],E[i],F[i],G[i],H[i]))
c.execute("SELECT * FROM bid")
print(c.fetchall())
conn.commit()
conn.close()
c.execute("DROP Table bid;")    
    
    
    
    
    
    
    
    
    
    

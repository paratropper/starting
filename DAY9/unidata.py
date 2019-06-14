# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:31:49 2019

@author: HP
"""

import sqlite3
from pandas import DataFrame

conn = sqlite3.connect ( 'university.db' )
c = conn.cursor()

c.execute ("""CREATE TABLE university(
          name TEXT,
          age  INTEGER,
          branch TEXT,
          roll_number INTEGER
          )""")

c.execute("INSERT INTO university VALUES ('raghu', 22,'CS', 200)")
c.execute("INSERT INTO university VALUES ('raghuu', 23,'CS', 201)")
c.execute("INSERT INTO university VALUES ('raghuuu', 24,'CS', 202)")
c.execute("INSERT INTO university VALUES ('raghuuuuu', 25,'CS', 203)")
c.execute("INSERT INTO university VALUES ('raghuuuuuu', 26,'CS', 204)")
c.execute("INSERT INTO university VALUES ('raghuuuuuuu', 27,'CS', 205)")
c.execute("INSERT INTO university VALUES ('raghuuuuuuuu', 28,'CS', 206)")
c.execute("INSERT INTO university VALUES ('raghuuuuuuuuu', 29,'CS', 207)")
c.execute("INSERT INTO university VALUES ('raghuuuuuuuuuu', 30,'CS', 208)")
c.execute("INSERT INTO university VALUES ('raghuuuuuuuuuuu', 31,'CS', 2009)")

c.execute("SELECT * FROM university")

print ( c.fetchall() )
c.execute("SELECT * FROM university")

df = DataFrame(c.fetchall())
df.columns = ["name","age","branch","roll_no"]

conn.commit()
conn.close()



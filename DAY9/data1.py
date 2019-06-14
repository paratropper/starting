# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:50:28 2019

@author: HP
"""

import pymongo

client = pymongo.MongoClient("mongodb://raghav:raghav%40123@cluster0-shard-00-00-fpcwy.mongodb.net:27017,cluster0-shard-00-01-fpcwy.mongodb.net:27017,cluster0-shard-00-02-fpcwy.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.universitydb

def add_student(name, age, branch, roll_no):
   
    db.student.insert_one(
            {
            "name" : name,
            "age" : age,
            "branch" : branch,
            "roll_no" : roll_no
            })
    return "student added successfully"

add_student ('raghu', 22,'CS', 200)
add_student ('raghuu', 23,'CS', 201)
add_student ('raghuuu', 24,'CS', 202)
add_student ('raghuuuuu', 25,'CS', 203)
add_student ('raghuuuuuu', 26,'CS', 204)
add_student ('raghuuuuuuu', 27,'CS', 205)
add_student ('raghuuuuuuuu', 28,'CS', 206)
add_student('raghuuuuuuuuu', 29,'CS', 207)
add_student ('raghuuuuuuuuuu', 30,'CS', 208)
add_student( 'raghuuuuuuuuuuu', 31,'CS', 2009)



def fetch_all_student():
    user = db.student.find()
    for i in user:
        print (i)
        
fetch_all_student()
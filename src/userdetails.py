'''
Author: Thrisha
Date: 04/04/2022

Version 1.0
Converted CSV writing to MongoDB
Version 1.1
'''
from src.db.dbconnection import *


def readuserdetailsbyuserid(user_id):
    userdetails = spuser.find({"userid":user_id})
    return userdetails

def readuserdetailsbyfirstname(first_name):
    userdetails = spuser.find({"firstname":first_name})
    return userdetails

def readuserdetailsbylastname(last_name):
    userdetails = spuser.find({"lastname":last_name})
    return userdetails

def readuserdetailsbypassword(password):
    userdetails = spuser.find({"password":password})
    return userdetails

def readuserdetailsbyphone(phone):
    userdetails = spuser.find({"phone":phone})
    return userdetails


record = readuserdetailsbyuserid("r")
for rec in record:
    print(rec)


spuser.find({"user_id":"001"}) 
spuser.update_one({"first_name": "daksha"},{"$set":{"last_name":"Muniyandi"}})
spuser.delete_one({"user_id":"001"})
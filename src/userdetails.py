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

#modify a single data
def updateuserdetailbyid(user_id, first_name, last_name, password, phone):
    spuser.update_one({"user_id":user_id},
        {"$set": {"first_name":first_name, 
        "last_name":last_name,"password":password, "phone":phone}})

#remove a specific data
def deleteuserdetailbyid(cow_id):
    spuser.delete_one({"user_id":"001"})
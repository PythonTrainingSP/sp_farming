'''
Author: Thrisha
Date: 04/04/2022

Version 1.0
Converted CSV writing to MongoDB
Version 1.1
'''
from db.dbconnection import *
from bson.json_util import dumps, loads

def readuserdetailsbyuserid(user_id):
    userdetails = spuser.find({"user_id":user_id})
    return userdetails

def readuserdetailsbyfirstname(first_name):
    userdetails = spuser.find({"first_name":first_name})
    return userdetails

def readuserdetailsbylastname(last_name):
    userdetails = spuser.find({"last_name":last_name})
    return userdetails

def readuserdetailsbypassword(password):
    userdetails = spuser.find({"password":password})
    return userdetails

def readuserdetailsbyphone(phone):
    userdetails = spuser.find({"phone":phone})
    return userdetails

#modify a single data
def adduserdetail(user_id, first_name, last_name, password, phone):
    #x = mycol.insert_one(mydict)
    spuser.insert_one({"user_id":user_id, "first_name":first_name, "last_name":last_name, "password":password, "phone":phone})

#modify a single data
def updateuserdetailbyid(user_id, first_name, last_name, password, phone):
    spuser.update_one({"user_id":user_id},
        {"$set": {"first_name":first_name, 
        "last_name":last_name,"password":password, "phone":phone}})

#remove a specific data
def deleteuserdetailbyid(cow_id):
    spuser.delete_one({"user_id":"001"})

@app.post("/update/user")
def update_user():
    if request.is_json:
        user = request.get_json()
    user_id = user["user_id"]
    first_name = user["first_name"]
    last_name = user["last_name"]
    password = user["password"]
    phone = user["phone"]
    #first_name = user["first_name"]
    updateuserdetailbyid(user_id,first_name, last_name, password, phone)
    return '{"ok"}'

@app.post("/add/user")
def add_user():
    if request.is_json:
        user = request.get_json()
    user_id = user["user_id"]
    first_name = user["first_name"]
    last_name = user["last_name"]
    password = user["password"]
    phone = user["phone"]
    #first_name = user["first_name"]
    adduserdetail(user_id,first_name, last_name, password, phone)
    return '{"ok"}'

@app.get('/find/user/<user_id>')
# ‘/’ URL is bound with hello_world() function.
def get_user(user_id):
    record = readuserdetailsbyuserid(user_id)     
    list_cur = list(record)
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) 
    return json_data
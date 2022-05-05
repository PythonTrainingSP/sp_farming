'''
Author: Thrisha
Date: 04/04/2022

Version 1.0
Converted CSV writing to MongoDB
Version 1.1
'''
from dbconnection import *


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


'''
record = {} #empty record for single record should be dic/JSON Object 
records = [] #empty record for multiple record

#reading user detail start
flag ='y'
while flag == 'y' or flag == 'Y':
    user_id = input('user id ')
    first_name = input('first name ')
    last_name = input('last name ')
    password = input('password ')
    phone = input('phone ')
    #reading user detail end
    
    #adding user detail into record start
    record["user_id"] = user_id
    record["first_name"] = first_name
    record["last_name"] = last_name
    record["password"] = password
    record["phone"] = phone
    
    records.append(record)#addingto records
    #adding user detail into record end
    flag = input('continue (y/n)')
    record = {}
    
#print(record) #user details
for record in records:
    spuser.insert_one(record)

    '''
record = readuserdetailsbytime("r")
for rec in record:
    print(rec)
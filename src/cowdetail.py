#This program is to read data from database

'''
Author: Brundha
Date: 6/5/2022

Version 1.0
Converted CSV writing to MongoDB

'''
from db.dbconnection import *             #only for writing db
from bson.json_util import dumps, loads

def readcowdetailbycowid(cow_id):
    cowdetail = spcow.find({"cow_id":cow_id})
    return cowdetail

def readcowdetailbybreed(breed):
    cowdetail = spcow.find({"breed":breed})
    return cowdetail

def readcowdetailbydob(dob):
    cowdetail = spcow.find({"dob": dob})
    return cowdetail

def readcowdetailbycolor(color):
    cowdetail = spcow.find({"color":color})
    return cowdetail

def readcowdetailbygender(gender):
    cowdetail = spcow.find({"gender":gender})
    return cowdetail

def readcowdetailbymilking(milking):
    cowdetail = spcow.find({"milking":milking})
    return cowdetail

def readcowdetailbygestationperiod(gestationperiod):
    cowdetail = spcow.find({"gestationperiod":gestationperiod})
    return cowdetail

def readcowdetailbyhealthstatus(healthstatus ):
    cowdetail = spcow.find({"healthstatus ":healthstatus })
    return cowdetail

def readcowdetailbyvaccinationschedule(vaccinationschedule):
    cowdetail = spcow.find({"vaccinationschedule":vaccinationschedule})
    return cowdetail

#modify a single data
def updatecowdetailbyid(cow_id, weight, healthstatus, vaccinationschedule):
    spcow.update_one({"cow_id":cow_id},
        {"$set": {"weight":weight, "healthstatus":healthstatus,"vaccinationschedule":vaccinationschedule }})

#remove a specific data
def deletecowdetailbyid(cow_id):
    spcow.delete_one({"cow_id":cow_id})


#Service

 
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function. 
@app.route('/cowdetail/<cow_id>')
# ‘/’ URL is bound with hello_world() function.
def getCowDetail(cow_id):
    record = readcowdetailbycowid(cow_id)  # for reading cow detail by id
    list_cur = list(record) # convert record into list
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) # convert as json object
    return json_data

@app.route('/cowdetailbyBreed/<breed>')
# ‘/’ URL is bound with hello_world() function.
def getCowDetailbyBreed(breed):
    record = readcowdetailbybreed(breed)  # for reading cow detail by breed
    list_cur = list(record) # convert record into list
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) # convert as json object
    return json_data

@app.route('/cowdetailByGender/<gender>')
# ‘/’ URL is bound with hello_world() function.
def getCowDetailbyGender(gender):
    record = readcowdetailbygender(gender)  # for reading cow detail by gender
    list_cur = list(record) # convert record into list
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) # convert as json object
    return json_data   

'''
@app.route('/userdetailsbyname/<first_name>') # http://localhost:5400/userdetailname/muni
# ‘/’ URL is bound with hello_world() function.
def getuserdetailsbyname(first_name):
    record = readuserdetailsbyfirstname(first_name)  # for reading userdetails by firstname
    list_cur = list(record) # convert record into list
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) # convert as json object
    return json_data   

@app.route('/userdetails/<user_id>') # http://localhost:5400/userdetail/0001
# ‘/’ URL is bound with hello_world() function.
def getuserdetails(user_id):
    record = readuserdetailsbyuserid(user_id)  # for reading userdetails by userid
    list_cur = list(record) # convert record into list
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) # convert as json object
    return json_data   

@app.route('/feeddetail') # http://localhost:5400/feeddetail
# ‘/’ URL is bound with hello_world() function.
def getFeedList():
    record = readfeedDetailList()            #for reading feeddetail list
    list_cur = list(record)
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2)  #convert as json object
    return json_data

@app.route('/milkingdetail/<customer_id>') # http://localhost:5400/milkingdetail/453
# ‘/’ URL is bound with hello_world() function.
def getMilingDetail(customer_id):
    record = readmilkingdetailbycustomerid(customer_id)        #readmilkingdetailbycustomerid

    list_cur = list(record)
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) 
    return json_data

@app.route('/milkingdetaillist') # http://localhost:5400/milkingdetaillist
# ‘/’ URL is bound with hello_world() function.
def getMilingDetailList():
    record = readmilkingdetaillist()              #readmilkingdetaillist    
    list_cur = list(record)
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) 
    return json_data


@app.route('/expensedetail/<transaction_date>')  #http://localhost:5400/expensedetail/
# ‘/’ URL is bound with hello_world() function.
def getexpensedetail(transaction_date):
    record = readexpensedetailbydate(transaction_date)       #read expense detail by date    
    list_cur = list(record)
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) 
    return json_data
'''


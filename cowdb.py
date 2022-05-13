#This program is to read data from database

'''
Author: Brundha
Date: 6/5/2022

Version 1.0
Converted CSV writing to MongoDB

'''
from dbconnection import *             #only for writing db

def readcowdetailbycowid(cow_id):
    cowdetail = spcow.find({"cowid":cow_id})
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

'''
record = {} #empty record for single record should be dic/JSON Object
records = [] #empty record for multiple record

flag = 'y'
while flag == 'y' or flag == 'Y':
     cow_id = input('Cow id? ')
    breed = input('Breed? ')
    dob = input('dob (dd/mm/yy)? ')
    weight = input('Weight? ')
    color = input('Color? ')
    healthstatus = input('Health status? ')
    gender = input('Gender (Male/Female)? ')
    if (gender.upper() == "female".upper() or gender.upper() == "f".upper()):
        milking = input('Milking (y/n)? ')
        gestationperiod = input('Gestationperiod (y/n)? ')

    #milking = input('Milking (y/n)? ')
    vaccinationschedule = input('Vaccination schedule (dd/mm/yy) ')
    #Reading Cow detail end

    #adding Cow detail into record start
    record["cow_id"] = cow_id 
    record["breed"] =  breed
    record["dob"] = dob
    record["weight"] = weight 
    record["color"] = color
    record["gender"] = gender
    if ((gender.upper() == "female".upper()) or (gender.upper() == 'f'.upper())):
        record["milking"] = milking
        record["gestationperiod"] = gestationperiod 
    record["healthstatus"] = healthstatus 
    record["vaccinationschedule"] =  vaccinationschedule
    
    records.append(record) # adding to recored
    #adding Cow detail into record end
    flag = input('Continue (y/n)? ')
    record = {} # empty record object

for record in records: # write one by one using for loop
     spcow.insert_one(record)

'''
record = readcowdetailbymilking("y")
for rec in record:
    print(rec)
    
     #reading specific data
    dbconnection.cow.find({"breed":"sindhi"})

    #modify a single data
    dbconnection.cow.updatemany({"breed":"gir"},{set{milking:yes}})

    #remove a specific data
    dbconnection.cow.remove({"gender":"male"})




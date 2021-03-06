'''
Author: Bhrundha
Date: 03/04/2022

Version 1.0
Converted CSV writing to MongoDB
Version 1.1
'''

from src.db.dbconnection import *

record = {} #empty record for single record should be dic/JSON Object
records = [] #empty record for multiple record

#reading user detail start
flag ='y'
while flag.lower() == 'y'.lower():
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


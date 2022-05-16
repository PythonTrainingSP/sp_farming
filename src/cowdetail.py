#This program is to read data from database

'''
Author: Brundha
Date: 6/5/2022

Version 1.0
Converted CSV writing to MongoDB

'''
from db.dbconnection import *             #only for writing db

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




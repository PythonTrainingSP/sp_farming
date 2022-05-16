'''
Author: surender
Date: 03/04/2022

Version 1.0
Converted CSV writing to MongoDB
Version 1.1

'''
from src.db.dbconnection import *

record = {}
records = []

flag = "Y"
while flag == "Y" or flag == "y":
    # Reading doctor visit detail start
     date = input('date of visit (dd/mm/yy)? ')
     name = input('doctorname  ')
     cow_id = input('Cow id? ')
     vaccineName = input('Vaccine name? ')
     vaccineType = input('Vaccine type? ')
     dose = float(input('Dose of a vaccine? '))
     fee = float(input('Doctor fee? '))

     record["date of visit"]= date
     record["doctorname"]= name
     record["cowid"]= cow_id
     record["vaccineName"]=vaccineName
     record[" vaccineType"]= vaccineType
     record["dose"]= dose
     record["fee"]= fee

     records.append(record)
     flag=input("continue y/n ")
     record={}

for record in records:
    spdoctorvisit.insert_one(record)
    

     
'''
Author: surendar
Date: 03/04/2022

Version 1.0
Converted CSV writing to MongoDB

'''

#this program created for addind doctor visit
from dbconnection import *

record = {}  # empty record for single record
records = []  # empty record for multiple record


flag = "Y"
while flag == "Y" or flag == "y":
    # Reading doctor visit detail start
     date = input('Date of visit (dd/mm/yy)? ')
     name = input('Doctor Name  ')
     cow_id = input('Cow id? ')
     vaccineName = input('Vaccine name? ')
     vaccineType = input('Vaccine type? ')
     dose = input('Dose of a vaccine? ')
     fee = float(input('Doctor fee? '))

      # Reading doctor visit detail end

    # adding doctor detail into record start
     record["date"]=date
     record["doctor_name"]=name
     record["cow_id"]=cow_id
     record["vaccine_name"]=vaccineName
     record["vaccine_type"]=vaccineType
     record["dose"]=dose
     record["fee"]=fee

     records.append(record)  # adding to record
    # adding doctor detail into record end
     flag = input('Continue (y/n)? ')
     record = {}         #empty record object

for record in records:
    spdoctorvisit.insert_one(record)
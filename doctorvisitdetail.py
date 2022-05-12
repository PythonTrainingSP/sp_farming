'''
Author: vijaya bharathi
Date: 12/05/2022

version 1.0
converted csv writing to mongodb
version 1.1
'''
from dbconnection import *

#only for writing DB
def readdoctordetailbydate (date):
    Doctordetail = spdoctorvisit.find({"date":date})
    return Doctordetail

def readdoctordetailbyname (name):
    Doctordetail = spdoctorvisit.find({"name":name})
    return Doctordetail

def readdoctordetailbycowid(Cow_id):
    Doctordetail = spdoctorvisit.find({"Cow_id":Cow_id})
    return Doctordetail

def readdoctordetailbyvaccinename(VaccineName):
    Doctordetail = spdoctorvisit.find({"VaccineName":VaccineName})
    return Doctordetail

def readdoctordetailbyvaccinetype(VaccineType):
    Doctordetail = spdoctorvisit.find({"VaccineType":VaccineType})
    return Doctordetail

def readdoctordetailbydose(dose):
    Doctordetail = spdoctorvisit.find({"dose":dose})
    return Doctordetail

def readdoctordetailbyfee(fee):
    Doctordetail = spdoctorvisit.find({"fee":fee})
    return Doctordetail

'''
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
     record["name"]=name
     record["cow_id"]=cow_id
     record["vaccineName"]=vaccineName
     record["vaccineType"]=vaccineType
     record["dose"]=dose
     record["fee"]=fee

     records.append(record)  # adding to record
    # adding doctor detail into record end
     flag = input('Continue (y/n)? ')
     record = {}         #empty record object
'''

for record in records:
    spdoctorvisit.insert_one(record)
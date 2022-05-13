'''
Author: vijaya bharathi
Date: 12/05/2022

version 1.0
converted csv writing to mongodb
version 1.1
'''
from src.db.dbconnection import *

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

#modify a single data
def updatedoctordetailbyid(date, cow_id, VaccineName, VaccineType, does):
    spcow.update_one({"cow_id":cow_id},
        {"$set": {"date":date, "cow_id":cow_id,"VaccineName":VaccineType}})

#remove a specific data
def deletedoctordetailbyid(cow_id):
    spcow.delete_one({"cow_id":cow_id})

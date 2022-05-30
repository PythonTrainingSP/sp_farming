from textwrap import indent
from doctorvisitdetail import *
from bson.json_util import dumps, loads
from flask import Flask, request

@app.get('/doctorvisitdetaillist') # http://localhost:5400/feeddetail
# ‘/’ URL is bound with hello_world() function.
def getdoctordetailList():
    record = readdoctordetaillist()  #for reading feeddetail list
    list_cur = list(record)
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) 
    return json_data

@app.route('/doctorvisitdetailbydate/<date>')
def getdocotordetailbydate(date):
    record = readdoctordetailbydate(date)
    list_cur = list(record)
    json_data = dumps(list_cur, indent = 2) 
    return json_data


@app.route('/doctorvisitdetailbyname/<name>')
def getdocotordetailbyname(name):
    record = readdoctordetailbyname(name)
    list_cur = list(record)
    json_data = dumps(list_cur, indent = 2) 
    return json_data

@app.route('/doctorvisitdetailbycow_id/<Cow_id>')
def getdocotordetailbycowid(Cow_id):
    record = readdoctordetailbycowid(Cow_id)
    list_cur = list(record)
    json_data = dumps(list_cur, indent = 2) 
    return json_data

@app.route('/doctorvisitdetailbyvaccineName/<VaccineName>')
def getdocotordetailbyvaccinename(VaccineName):
    record = readdoctordetailbyvaccinename(VaccineName)
    list_cur = list(record)
    json_data = dumps(list_cur, indent = 2) 
    return json_data

@app.route('/doctorvisitdetailbyVaccineType/<VaccineType>')
def getdocotordetailbyvaccinetype(VaccineType):
    record = readdoctordetailbyvaccinetype(VaccineType)
    list_cur = list(record)
    json_data = dumps(list_cur, indent = 2) 
    return json_data

@app.route('/doctorvisitdetailbydose/<dose>')
def getdocotordetailbydoes(dose):
    record = readdoctordetailbydose(dose)
    list_cur = list(record)
    json_data = dumps(list_cur, indent = 2) 
    return json_data

@app.route('/doctorvisitdetailbyfee/<fee>')
def getdocotordetailbyfee(fee):
    record = readdoctordetailbyfee(fee)
    list_cur = list(record)
    json_data = dumps(list_cur, indent = 2) 
    return json_data

@app.post("/update/doctorvisit")
def update_doctorvisit():
    if request.is_json:
        doctorvisit = request.get_json()
    date =doctorvisit["date"]
    name=doctorvisit["name"]
    cow_id=doctorvisit["cow_id"]
    VaccineName=doctorvisit["VaccineName"]
    VaccineType=doctorvisit["VaccineType"]
    dose=doctorvisit["dose"]
    updatedoctordetailbyid(date,name,cow_id, VaccineName,VaccineType,dose)
    return '{"ok"}'

@app.post("/add/doctorvisit")
def add_doctorvisit():
    if request.is_json:
        doctorvisit = request.get_json()
    date =doctorvisit["date"]
    name=doctorvisit["name"]
    cow_id=doctorvisit["cow_id"]
    VaccineName=doctorvisit["VaccineName"]
    VaccineType=doctorvisit["VaccineType"]
    dose=doctorvisit["dose"]
    updatedoctordetailbyid(date,name,cow_id, VaccineName,VaccineType,dose)
    return '{"ok"}'

@app.get('/find/doctorvisit/<cow_id>')
# ‘/’ URL is bound with hello_world() function.
def get_doctorvisit(cow_id):
    record = readdoctordetailbycowid(cow_id)     
    list_cur = list(record)
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) 
    return json_data

@app.delete('/find/doctorvisit/<cow_id>')
# ‘/’ URL is bound with hello_world() function.
def delete_doctorvisit(cow_id):
    record = readdoctordetailbycowid(cow_id)     
    list_cur = list(record)
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) 
    return json_data

if __name__ == "__main__":
    app.run()

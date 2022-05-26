from textwrap import indent
from cowdetail import *
from bson.json_util import dumps, loads
from flask import Flask, request

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function. 


@app.route('/cowdetail/<cow_id>')
# ‘/’ URL is bound with hello_world() function.
def getCowDetailbycowid(cow_id):
    record = readcowdetailbycowid(cow_id)  # for reading cow detail by id
    list_cur = list(record) # convert record into list
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) # convert as json object
    return json_data

@app.route('/cowdetailbyBreed/<breed>')
# ‘/’ URL is bound with hello_world() function.
def getCowDetailbybreed(breed):
    record = readcowdetailbybreed(breed)  # for reading cow detail by breed
    list_cur = list(record) # convert record into list
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) # convert as json object
    return json_data

@app.route('/cowdetailbygender/<gender>')
# ‘/’ URL is bound with hello_world() function.
def getCowDetailbyGender(gender):
    record = readcowdetailbygender(gender)  # for reading cow detail by gender
    list_cur = list(record) # convert record into list
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) # convert as json object
    return json_data  

@app.route('/cowdetailbydob/<dob>')          # http://localhost:5400/feeddetail
# ‘/’ URL is bound with hello_world() function.
def getcowdetaibydob(dob):
    record = readcowdetailbydob(dob)            #for reading cow detail by date of birth
    list_cur = list(record)
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2)  #convert as json object
    return json_data

@app.route('/cowdetailbymiking/<milking>')          # http://localhost:5400/feeddetail
# ‘/’ URL is bound with hello_world() function.
def getcowdetaibymilking(milking):
    record = readcowdetailbymilking(milking)            #for reading cow detail by date of birth
    list_cur = list(record)
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2)  #convert as json object
    return json_data

@app.post("/update/cow")
def update_cow():
    if request.is_json:
        cow = request.get_json()
    cow_id = cow["cow_id"]
    weight = cow["weight"]
    healthstatus = cow["healthstatus"]
    vaccinationschedule= cow["vaccinationschedule"]
    
    updatecowdetailbyid(cow_id, weight, healthstatus, vaccinationschedule)
    return '{"ok"}'

@app.post("/add/cow")
def add_cow():
    if request.is_json:
        cow = request.get_json()
    print("Enter into add_cow", cow)
    cow_id = cow["cow_id"]
    breed = cow["breed"]
    dob = cow["dob"]
    color = cow["color"]
    gender = cow["gender"]
    weight = cow["weight"]
    healthstatus = cow["healthstatus"]
    vaccinationschedule = cow["vaccinationschedule"]
    addcowdetail(cow_id, breed, dob, weight, color, gender, 
        healthstatus, vaccinationschedule)
    return '{"ok"}'

@app.get('/find/cow/<cow_id>')
# ‘/’ URL is bound with hello_world() function.
def get_cow(cow_id):
    record = readcowdetailbycowid(cow_id)     
    list_cur = list(record)
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) 
    return json_data

@app.delete('/delete/cow/<cow_id>')
# ‘/’ URL is bound with hello_world() function.
def delete_cow(cow_id):
    record = readcowdetailbycowid(cow_id)     
    list_cur = list(record)
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) 
    return json_data
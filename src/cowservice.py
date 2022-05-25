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


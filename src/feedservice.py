from textwrap import indent
from feeddetail import *
from bson.json_util import dumps, loads
from flask import Flask, request

@app.route('/feeddetail') # http://localhost:5400/feeddetail
# ‘/’ URL is bound with hello_world() function.
def getFeedList():
    record = readfeedDetailList()            #for reading feeddetail list
    list_cur = list(record)
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2)  #convert as json object
    return json_data

@app.route('/feeddetailbydate/<date>')
def getfeeddetailbydate(date):
    record = readfeedDetailbydate(date)
    list_cur = list(record)
    json_data = dumps(list_cur, indent = 2)
    return json_data


@app.route('/feeddetailbytime/<time>')
def getfeeddetailbytime(time):
    record = readfeeddetailbytime(time)
    list_cur = list(record)
    json_data = dumps(list_cur, indent = 2)
    return json_data

@app.route('/feeddetailbyquantity/<quantity>')
def getfeeddetailbyquantity(quantity):
    record = readfeeddetailbyquantity(quantity)
    list_cur = list(record)
    json_data = dumps(list_cur, indent=2)
    return json_data

@app.route('/feeddetailbytypesoffeed/<types_of_feed>')
def getfeeddetailbytypesoffeed(types_of_feed):
    record = readfeeddetailbytypesoffeed(types_of_feed)
    list_cur = list(record)
    json_data = dumps(list_cur, indent=2)
    return json_data

@app.route('/feeddetailbywatering/<watering>')
def getfeeddetailbywatering(watering):
    record = readfeeddetailbywatering(watering)
    list_cur = list(record)
    json_data = dumps(list_cur, indent=2)
    return json_data

@app.route('/feeddetailbyotherminerals/<other_minerals>')
def getfeeddetailbyotherminerals(other_minerals):
    record = readfeeddetailbyotherminerals(other_minerals)
    list_cur = list(record)
    json_data = dumps(list_cur, indent=2)
    return json_data


@app.post("/update/feed")
def update_feed():
    if request.is_json:
        feed = request.get_json()
    date =feed["date"]
    time=feed["time"]
    types_of_feed=feed["types_of_feed"]
    quantity=feed["quantity"]
    watering=feed["watering"]
    other_minerals=feed["other_minerals"]
    updatefeeddetailbydate(date,time,types_of_feed,quantity,watering,other_minerals)
    return '{"ok"}'

@app.post("/add/feed")
def add_feed():
    if request.is_json:
        feed = request.get_json()
    date =feed["date"]
    time=feed["time"]
    types_of_feed=feed["types_of_feed"]
    quantity=feed["quantity"]
    watering=feed["watering"]
    other_minerals=feed["other_minerals"]
    addfeeddetail(date,time,types_of_feed,quantity,watering,other_minerals)
    return '{"ok"}'


@app.get('/find/feed/<time>')
# ‘/’ URL is bound with hello_world() function.
def get_feed(time):
    record = readfeeddetailbytime(time)     
    list_cur = list(record)
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) 
    return json_data


@app.delete('/find/feed/<time>')
def delete_feed(time):
    record = readfeeddetailbytime(time)
    list_cur = list(record)
    json_data = dumps(list_cur, indent = 2) 
    return json_data


if __name__ == "__main__":
    app.run()

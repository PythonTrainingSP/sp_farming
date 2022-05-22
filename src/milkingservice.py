from re import M
from milkingdetail import *
from bson.json_util import dumps, loads
from flask import Flask, request

app = Flask(__name__)
@app.route('/milkingdetaillist')
# ‘/’ URL is bound with hello_world() function.
def getMilkingDetailList():
    record = readmilkingdetaillist()     
    list_cur = list(record)
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) 
    return json_data

@app.route('/milkingdetailbycustomerid/<customer_id>')
# ‘/’ URL is bound with hello_world() function.
def getMilkingDetailbycustomerid(customer_id):
    record = readmilkingdetailbycustomerid(customer_id)    
    list_cur = list(record)
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) 
    return json_data

@app.route('/milkingdetailbydate/<date>')
# ‘/’ URL is bound with hello_world() function.
def getMilkingDetailbydate(date):
    record = readmilkingdetailbydate(date)    
    list_cur = list(record)
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) 
    return json_data


@app.route('/milkingdetailbytime/<time>')
# ‘/’ URL is bound with hello_world() function.
def getMilkingDetailbytime(time):
    record = readmilkingdetailbytime(time)    
    list_cur = list(record)
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) 
    return json_data

@app.route('/milkingdetailbyquantity/<quantity>')
# ‘/’ URL is bound with hello_world() function.
def getMilkingDetailbyquantity(quantity):
    record = readmilkingdetailbyquantity(quantity)    
    list_cur = list(record)
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) 
    return json_data


@app.route('/milkingdetailbyfat/<fat>')
# ‘/’ URL is bound with hello_world() function.
def getMilkingDetailbyfat(fat):
    record = readmilkingdetailbyfat(fat)    
    list_cur = list(record)
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) 
    return json_data

@app.route('/milkingdetailbysnf/<snf>')
# ‘/’ URL is bound with hello_worldunction.
def getMilkingDetailbysnf(snf):
    record = readmilkingdetailbysnf(snf)    
    list_cur = list(record)
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) 
    return json_data
 
@app.route('/milkingdetailbyprice/<price>')
# ‘/’ URL is bound with hello_world() function.
def getMilkingDetailbyprice(price):
    record = readmilkingdetailbyprice(price)    
    list_cur = list(record)
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) 
    return json_data


@app.post("/milking")
def add_milking():
    if request.is_json:
        milking = request.get_json()
    customer_id = milking["customer_id"]
    date =milking["date"]
    time=milking["time"]
    quantity=milking["quantity"]
    fat=milking["fat"]
    snf=milking["snf"]
    price=milking["price"]
  
    updatemilkingdetailcustomerid(customer_id,date,time,quantity,fat,snf,price)
    return '{"ok"}'


if __name__ == "__main__":
    app.run()
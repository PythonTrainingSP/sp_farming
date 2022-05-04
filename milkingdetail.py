'''
Author: Murali
Date: 03/04/2022

Version 1.0
Converted CSV writing to MongoDB
Version 1.1
'''
from dbconnection import *

record = {} #empty record for single record should be dic/JSON Object
records = [] #empty record for multiple record

flag = 'y'
while flag == 'y' or flag == 'Y':
    customer_id = input("Customer Id ")
    date = input('Date ')
    time = input('Time (M/E) ')
    quantity = float(input('Quantity '))
    fat  = float(input('Fat '))
    snf  = float(input('SnF '))
    price = float(input('Price per liter '))
    amount = quantity * price
    

    #adding milking detail into record start
    record["customer_id"]  = customer_id
    record["date"] = date
    record["time"] = time
    record["quantity"] = quantity
    record["fat"] = fat
    record["snf"] = snf
    record["price"] = price
    record["amount"] = amount
    
    records.append(record) # adding to recored
    #adding milking detail into record end
    flag = input('Continue (y/n)? ')
    record = {}
    
for record in records:
    spmilking.insert_one(record)
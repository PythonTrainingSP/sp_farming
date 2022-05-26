'''
Author: Murali
Date: 03/04/2022

Version 1.0
Converted CSV writing to MongoDB
Version 1.1
'''
from db.dbconnection import *

def readmilkingdetaillist():
    milkingdetail = spmilking.find()
    return milkingdetail

def readmilkingdetailbycustomerid(customer_id):
    milkingdetail = spmilking.find({"customer_id":customer_id})
    return milkingdetail

def readmilkingdetailbydate(date):
    milkingdetail = spmilking.find({"date":date})
    return milkingdetail

def readmilkingdetailbytime(time):
    milkingdetail = spmilking.find({"time":time})
    return milkingdetail

def readmilkingdetailbyquantity(quantity):
    milkingdetail = spmilking.find({"quantity":quantity})
    return milkingdetail

def readmilkingdetailbyfat(fat):
    milkingdetail = spmilking.find({"fat":fat})
    return milkingdetail

def readmilkingdetailbysnf(snf):
    milkingdetail = spmilking.find({"snf":snf})
    return milkingdetail

def readmilkingdetailbyprice(price):
    milkingdetail = spmilking.find({"price":price})
    return milkingdetail


'''
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
'''

def addmilkingdetail(customer_id, date, time, quantity, fat, snf, price):
    spmilking.insert_one({"customer_id":customer_id, "date":date, "time":time, "quantity":quantity, "fat":fat, "snf":snf, "price":price})
#modify a single data
def updatemilkingdetailcustomerid(customer_id, date, time, quantity, fat, snf, price,):
    spmilking.update_one({"customer_id":customer_id}, {"$set":{"date":date, "time":time, "quantity":quantity, "fat":fat, "snf":snf, "price":price }})

#remove specific data
def deletemilkingdetailcustomerid(customer_id):
    spmilking.delete_one({"customer_id":"345"})
    

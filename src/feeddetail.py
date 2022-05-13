'''
Author: Marthu
Date: 03/04/2022

Version 1.0
Converted CSV writing to MongoDB
Version 1.1
'''

from src.db.dbconnection import *

#only for writing DB
def readfeedDetailbydate(date):
    feeddetail = spfeed.find({"date":date})
    return feeddetail
    
def readfeeddetailbytime(time):
    feeddetail = spfeed.find({"time":time})
    return feeddetail

def readfeeddetailbytypesoffeed(types_of_feed):
    feeddetail =spfeed.find({"types of feed":types_of_feed})
    return feeddetail

def readfeeddetailbyquantity(quantity):
    feeddetail = spfeed.find({"quantity":quantity})
    return feeddetail

def readfeeddetailbywatering(watering):
    feeddetail = spfeed.find({"watering":watering})
    return feeddetail

def readfeeddetailbyotherminerals(other_minerals):
    feeddetail = spfeed.find({"other minerals":other_minerals})
    return feeddetail



'''

record = {} #empty record for single record should be dic/JSON Object
records = [] #empty record for multiple record

flag="y"
while flag=="y" or flag=="Y":
    date=input("Date: ")
    time=input("Time (Morning/Noon/Evening/Night): ")
    types_of_feed=input("Types of feed: ")
    quantity=float(input("quantity: "))
    watering=float(input("watering: "))
    other_minerals=input("Other Minerals: ")
    
    record["date"] = date
    record["time"] = time
    record["types_of_feed"] = types_of_feed
    record["quantity"] = quantity
    record["watering"] = watering
    record["other_minerals"] =other_minerals
    
    records.append(record)
    flag=input("continue(y/n)" )
    record = {}
    
#print(record) #user details
for record in records:
    spfeed.insert_one(record)

'''  
#modify a single data
def updatefeeddetailbydate(date, time, types_of_feed, quantity, watering, other_minerals):
    spfeed.update_one({"date":date}, {"$set": {"time":time, "typesoffeed":types_of_feed, "quantity":quantity, "watering":watering, "otherminerals":other_minerals}})

#remove a specific data
def removefeeddetailbydate(date):
    spfeed.delete_one({"date":"03/05/2022"})
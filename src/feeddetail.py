'''
Author: Marthu
Date: 03/04/2022

Version 1.0
Converted CSV writing to MongoDB
Version 1.1
'''

from db.dbconnection import *


#only for writing DB
def readfeedDetailList():
    feeddetail = spfeed.find()
    return feeddetail

#only for writing DB 03-03-1972
def readfeedDetailbydate(date):
    #date = date.split("-")
    #date = date[0] + "/" + date[1] + "/" + date[2] 
    date = date.replace("-","/")
    feeddetail = spfeed.find({"date":date})
    return feeddetail
    
def readfeeddetailbytime(time):
    feeddetail = spfeed.find({"time":time})
    return feeddetail

def readfeeddetailbytypesoffeed(types_of_feed):
    feeddetail =spfeed.find({"types_of_feed":types_of_feed})
    return feeddetail

def readfeeddetailbyquantity(quantity):
    quantity = int(quantity)
    feeddetail = spfeed.find({"quantity":quantity})
    return feeddetail

def readfeeddetailbywatering(watering):
    feeddetail = spfeed.find({"watering":watering})
    return feeddetail

def readfeeddetailbyotherminerals(other_minerals):
    feeddetail = spfeed.find({"other_minerals":other_minerals})
    return feeddetail

def addfeeddetail(date,time,types_of_feed,quantity,watering,other_minerals):
    spfeed.insert_one({"date":date, "time":time, "types_of_feed":types_of_feed, 
    "quantity":quantity, "watering":watering, "other_minerals":other_minerals})

#modify a single data
def updatefeeddetailbydate(date, time, types_of_feed, quantity, watering, other_minerals):
    spfeed.update_one({"date":date}, {"$set": {"time":time, "types_of_feed":types_of_feed, 
    "quantity":quantity, "watering":watering, "other_minerals":other_minerals}})

#remove a specific data
def deletefeeddetailbydate(date):
    spfeed.delete_one({"date":"03/05/2022"})
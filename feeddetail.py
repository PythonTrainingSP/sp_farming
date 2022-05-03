from dbconnection import *

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
    
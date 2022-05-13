'''
Author: Maruth
Date: 03/04/2022

Version 1.0
Converted CSV writing to MongoDB
Version 1.1
'''

from src.db.dbconnection import *

record = {} #empty record for single record should be dic/JSON Object
records = [] #empty record for multiple record

flag="y"
while flag=="y" or flag=="Y":
    transaction_date = input('Transcation Date ')
    type_expense = input('Expense Type (Worker/Food/Doctor/Maintenance) ')
    amount = float(input('Amount (Rs) '))

    record["transaction_date"] = transaction_date
    record["type_expense"] = type_expense
    record["amount"] = amount
    
    records.append(record)
    flag=input("continue(y/n)" )
    record = {}
    
#print(record) #user details
for record in records:
    spexpense.insert_one(record)


from db.dbconnection import *
def readexpensedetaillist():
    expensedetail = spexpense.find()
    return expensedetail

def readexpensedetailbydate(transaction_date):
    expensedetail = spexpense.find({"transaction_date":transaction_date})
    return expensedetail

def readexpensedetailbytype(type_expense):
    expensedetail = spexpense.find({"type_expense":type_expense})
    return expensedetail

def readexpensedetailbyamount(amount):
    expensedetail = spexpense.find({"amount":amount})
    return expensedetail


#modify a single data
def updateexpensedetailbydate(transaction_date, type_expense, amount):
    spexpense.update_one({"transaction_date":transaction_date}, {"$set": {"type_expense":type_expense, "amount":amount}})

#remove a specific data
def removeexpensedetailbydate(transaction_date):
    spexpense.delete_one({"date":""})
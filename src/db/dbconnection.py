# 
import pymongo
from flask import Flask,request, jsonify

# connection string to connect into DB
dbconnection = "mongodb+srv://user123:user123@cluster0.gpfxv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
#command to connect
app = Flask(__name__)
spclient = pymongo.MongoClient(dbconnection)
#DB name
spdb = spclient["spfarming"]
#document or table for user
spuser = spdb["userdetail"]
#document or table for cow
spcow = spdb["cowdetail"]
#document or table for feed
spfeed = spdb["feeddetail"]
#document or table for expense
spexpense = spdb["expensedetail"]
#document or table for milking
spmilking = spdb["milkingdetail"]
#document or table for doctor visit
spdoctorvisit = spdb["doctorvisitdetail"]

#git config --global user.name "PythonTrainingSP"
#git config --global user.email "pythontraning737@gmail.com"

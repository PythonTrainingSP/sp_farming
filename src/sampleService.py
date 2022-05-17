# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
#from unicodedata import name
from feeddetail import *
from milkingdetail import *
from cowdetail import *  # to include cow function
from userdetails import *
from expensedetail import *
from bson.json_util import dumps, loads
from flask import Flask
from userdetails import readuserdetailsbyfirstname # convert all my function as service, then only i can access from browser
  
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
  
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function. 
@app.route('/cowdetail/<cow_id>')
# ‘/’ URL is bound with hello_world() function.
def getCowDetail(cow_id):
    record = readcowdetailbycowid(cow_id)  # for reading cow detail by id
    list_cur = list(record) # convert record into list
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) # convert as json object
    return json_data

@app.route('/cowdetail/<breed>')
# ‘/’ URL is bound with hello_world() function.
def getCowDetail(breed):
    record = readcowdetailbybreed(breed)  # for reading cow detail by breed
    list_cur = list(record) # convert record into list
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) # convert as json object
    return json_data

@app.route('/cowdetail/<gender>')
# ‘/’ URL is bound with hello_world() function.
def getCowDetail(gender):
    record = readcowdetailbygender(gender)  # for reading cow detail by gender
    list_cur = list(record) # convert record into list
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) # convert as json object
    return json_data   


@app.route('/userdetailsbyname/<first_name>') # http://localhost:5400/userdetailname/muni
# ‘/’ URL is bound with hello_world() function.
def getuserdetails(first_name):
    record = readuserdetailsbyfirstname(first_name)  # for reading userdetails by firstname
    list_cur = list(record) # convert record into list
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) # convert as json object
    return json_data   

@app.route('/userdetails/<user_id>') # http://localhost:5400/userdetail/0001
# ‘/’ URL is bound with hello_world() function.
def getuserdetails(user_id):
    record = readuserdetailsbyuserid(user_id)  # for reading userdetails by userid
    list_cur = list(record) # convert record into list
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) # convert as json object
    return json_data   

@app.route('/feeddetail') # http://localhost:5400/feeddetail
# ‘/’ URL is bound with hello_world() function.
def getFeedList():
    record = readfeedDetailList()            #for reading feeddetail list
    list_cur = list(record)
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2)  #convert as json object
    return json_data

@app.route('/milkingdetail/<customer_id>') # http://localhost:5400/milkingdetail/453
# ‘/’ URL is bound with hello_world() function.
def getMilingDetail(customer_id):
    record = readmilkingdetailbycustomerid(customer_id)        #readmilkingdetailbycustomerid

    list_cur = list(record)
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) 
    return json_data

@app.route('/milkingdetaillist') # http://localhost:5400/milkingdetaillist
# ‘/’ URL is bound with hello_world() function.
def getMilingDetailList():
    record = readmilkingdetaillist()              #readmilkingdetaillist    
    list_cur = list(record)
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) 
    return json_data


@app.route('/expensedetail/<transaction_date>')  #http://localhost:5400/expensedetail/
# ‘/’ URL is bound with hello_world() function.
def getexpensedetail(transaction_date):
    record = readexpensedetailbydate(transaction_date)       #read expense detail by date    
    list_cur = list(record)
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) 
    return json_data



# main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
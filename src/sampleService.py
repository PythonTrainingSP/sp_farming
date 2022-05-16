# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
#from unicodedata import name
from feeddetail import *
from milkingdetail import *
from cowdetail import *  # to include cow function
from bson.json_util import dumps, loads
from flask import Flask # convert all my function as service, then only i can access from browser
  
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
  
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function. 
@app.route('/cowdetail/<cowid>')
# ‘/’ URL is bound with hello_world() function.
def getCowDetail(cowid):
    record = readcowdetailbycowid(cowid)  # for reading cow detail by id
    list_cur = list(record) # convert record into list
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) # convert as json object
    return json_data

@app.route('/feeddetail')
# ‘/’ URL is bound with hello_world() function.
def getFeedList():
    record = readfeedDetailList()
    list_cur = list(record)
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) 
    return json_data

@app.route('/milkingdetail/<customerid>')
# ‘/’ URL is bound with hello_world() function.
def getMilingDetail(customerid):
    record = readmilkingdetailbycustomerid(customerid)
    list_cur = list(record)
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) 
    return json_data

@app.route('/milkingdetaillist')
# ‘/’ URL is bound with hello_world() function.
def getMilingDetailList():
    record = readmilkingdetaillist()
    list_cur = list(record)
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) 
    return json_data

#readmilkingdetaillist    

#readmilkingdetailbycustomerid

# main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
#from unicodedata import name
from feeddetail import *
from bson.json_util import dumps, loads
from flask import Flask
  
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
  
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function. 
@app.route('/feeddetail/<cowid>')
# ‘/’ URL is bound with hello_world() function.
def getFeedDetail(cowid):
    record = readfeeddetailbytime("night")
    list_cur = list(record)
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) 
    return json_data

@app.route('/feeddetail')
# ‘/’ URL is bound with hello_world() function.
def getFeedList():
    record = readfeeddetail()
    list_cur = list(record)
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) 
    return json_data

# main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
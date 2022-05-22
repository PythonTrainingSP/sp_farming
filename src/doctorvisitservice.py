from doctorvisitdetail import *
from bson.json_util import dumps, loads
from flask import Flask
app = Flask(__name__)

@app.route('/doctorvisitdetaillist') # http://localhost:5400/feeddetail
# ‘/’ URL is bound with hello_world() function.
def getdoctorvisitDetailList():
    record = readdoctorvisitDetaillist()  #for reading feeddetail list
    list_cur = list(record)
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) 
    return json_data

    @app.route('/doctorvisitdetail/<date>')

def getdocotorvisitDetail(date):
    record = readdoctorvisitdetailbydate(date)
    list_cur = list(record)

    json_data = dumps(list_cur, indent = 2) 
    return json_data

    if __name__ == '__main__':
         app.run()
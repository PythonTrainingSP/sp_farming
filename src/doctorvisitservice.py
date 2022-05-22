from doctorvisitdetail import *
from bson.json_util import dumps, loads
from flask import Flask
app = Flask(__name__)

@app.route('/doctorvisitdetaillist') # http://localhost:5400/feeddetail
# ‘/’ URL is bound with hello_world() function.
def getdoctordetailList():
    record = readdoctordetaillist()  #for reading feeddetail list
    list_cur = list(record)
    # Converting to the JSON
    json_data = dumps(list_cur, indent = 2) 
    return json_data

@app.route('/doctorvisitdetail/<date>')
def getdocotordetailbydate(date):
    record = readdoctordetailbydate(date)
    list_cur = list(record)
    json_data = dumps(list_cur, indent = 2) 
    return json_data

@app.route('/doctorvisitdetail/<name>')
def getdocotordetailbydate(name):
    record = readdoctordetailbydate(name)
    list_cur = list(record)
    json_data = dumps(list_cur, indent = 2) 
    return json_data

@app.route('/doctorvisitdetail/<Cow_id>')
def getdocotordetailbydate(Cow_id):
    record = readdoctordetailbydate(Cow_id)
    list_cur = list(record)
    json_data = dumps(list_cur, indent = 2) 
    return json_data

@app.route('/doctorvisitdetail/<VaccineName>')
def getdocotordetailbydate(VaccineName):
    record = readdoctordetailbydate(VaccineName)
    list_cur = list(record)
    json_data = dumps(list_cur, indent = 2) 
    return json_data

@app.route('/doctorvisitdetail/<VaccineType>')
def getdocotordetailbydate(VaccineType):
    record = readdoctordetailbydate(VaccineType)
    list_cur = list(record)
    json_data = dumps(list_cur, indent = 2) 
    return json_data

@app.route('/doctorvisitdetail/<does>')
def getdocotordetailbydate(does):
    record = readdoctordetailbydate(does)
    list_cur = list(record)
    json_data = dumps(list_cur, indent = 2) 
    return json_data

    @app.route('/doctorvisitdetail/<fee>')
def getdocotordetailbydate(fee):
    record = readdoctordetailbydate(fee)
    list_cur = list(record)
    json_data = dumps(list_cur, indent = 2) 
    return json_data




    if __name__ == '__main__':
         app.run()
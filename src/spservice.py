# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
#from unicodedata import name
from feeddetail import *
from feedservice import *

from milkingdetail import *
from milkingservice import *

from cowdetail import *  
from cowservice import *

from userdetails import *

from expensedetail import *


from doctorvisitdetail import *
from doctorvisitservice import *
  
from feeddetail import *
from feedservice import *
# Flask constructor takes the name of 
# current module (__name__) as argument.
   
# main driver function
if __name__ == '__main__':
  
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()
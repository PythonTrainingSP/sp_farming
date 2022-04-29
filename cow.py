#this program created for addind cow detail
from csv import writer             #creating a csv file imported library

out = writer(open("cow.csv", "a"))         #creating output file w mode always creat a new file
record = [] #empty record for single record
records = [] #empty record for multiple record

#Reading Cow detail start
flag = 'y'

while flag.lower() == 'y'.lower():  # Testing Python Training  Code
    cow_id = input('Cow id? ')
    breed = input('Breed? ')
    dob = input('Bob (dd/mm/yy)? ')
    weight = input('Weight? ')
    color = input('Color? ')
    healthstatus = input('Health status? ')
    gender = input('Gender (Male/Female)? ')
    if (gender.upper() == "female".upper() or gender.upper() == "f".upper()):
        milking = input('Milking (y/n)? ')
        gestationperiod = input('Gestationperiod (y/n)? ')

    #milking = input('Milking (y/n)? ')
    vaccinationschedule = input('Vaccination schedule (dd/mm/yy) ')
    #Reading Cow detail end

    #adding Cow detail into record start
    record.append(cow_id) 
    record.append(breed) 
    record.append(dob) 
    record.append(weight) 
    record.append(color) 
    record.append(gender) 
    if ((gender.upper() == "female".upper()) or (gender.upper() == 'f'.upper())):
        record.append(milking) 
        record.append(gestationperiod) 
    record.append(healthstatus) 
    record.append(vaccinationschedule) 
    
    records.append(record) # adding to recored
    #adding Cow detail into record end
    flag = input('Continue (y/n)? ')
    record = [] # empty record object

for record in records: # write one by one using for loop
    out.writerow(record) # writing to output file

  #modified cow csv file
    #modified file for git
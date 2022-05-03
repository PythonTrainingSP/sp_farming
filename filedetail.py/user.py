#this program created for addind user
from csv import writer

out = writer(open("user.csv","a"))
record = [] #empty record for single record 
records = [] #empty record for multiple record

#reading user detail start
flag ='y'
while flag == 'y' or flag == 'Y':
    user_id = input('user id ')
    first_name = input('first name ')
    last_name = input('last name ')
    password = input('password ')
    phone = input('phone ')
    #reading user detail end
    
    #adding user detail into record start
    record.append(user_id)
    record.append(first_name)
    record.append(last_name)
    record.append(password)
    record.append(phone)
    
    records.append(record)#addingto records
    #adding user detail into record end
    flag = input('continue (y/n)')
    record = [] 
    
print(record) #user details
for record in records:
    out.writerow(record)#writing to output file
    
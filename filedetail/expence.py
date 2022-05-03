#this program created for addind expence
   
from csv import writer

out = writer(open("expense.csv", "w"))         #creating output file
record = [] #empty record for single record
records = [] #empty record for multiple record


flag = 'y'
while flag == 'y' or flag == 'Y':
    #Reading Expense detail start
    transaction_date = input('Transcation Date ')
    type_expense = input('Expense Type (Worker/Food/Doctor/Maintenance) ')
    amount = float(input('Amount (Rs) '))
    #Reading Expense detail end

    #adding Expense detail into record start
    record.append(transaction_date) 
    record.append(type_expense) 
    record.append(amount) 
    records.append(record) # adding to recored
    #adding Expense detail into record end
    record = []
    flag = input('Continue (y/n)? ')

#print(record) #user details
for record in records:
    out.writerow(record)

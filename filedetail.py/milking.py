from csv import writer

out = writer(open("milking.csv", "a"))         #creating output file
record = [] #empty record for single record
records = [] #empty record for multiple record

#Reading Cow detail start
flag = 'y'
while flag == 'y' or flag == 'Y':
    customer_id = input("Customer Id ")
    date = input('Date ')
    time = input('Time (M/E) ')
    quantity = float(input('Quantity '))
    fat  = float(input('Fat '))
    snf  = float(input('SnF '))
    price = float(input('Price per liter '))
    amount = quantity * price
    #calculating amount
    
    #Reading Cow detail end

    #adding Cow detail into record start
    record.append(customer_id) 
    record.append(date) 
    record.append(time) 
    record.append(quantity) 
    record.append(fat) 
    record.append(snf) 
    record.append(price) 
    record.append(amount) 
    
    records.append(record) # adding to recored
    #adding Cow detail into record end
    flag = input('Continue (y/n)? ')
    record = []

for record in records:
    out.writerow(record) # writing to output file

    
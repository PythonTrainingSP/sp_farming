#this program created for addind feed
   
from csv import writer
out=writer(open("feeding.csv", "a"))
record= []
records=[]
flag="y"
while flag=="y" or flag=="Y":
    date=input("Date: ")
    time=input("Time (Morning/Noon/Evening/Night): ")
    types_of_feed=input("Types of feed: ")
    quantity=float(input("quantity: "))
    watering=float(input("watering: "))
    other_minerals=input("Other Minerals: ")
    
    record.append(date)
    record.append(time)
    record.append(types_of_feed)
    record.append(quantity)
    record.append(watering)
    record.append(other_minerals)
    
    records.append(record)
    flag=input("continue(y/n)" )
    record=[]
    
for record in records:
    out.writerow(record)

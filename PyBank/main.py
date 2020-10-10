import os
import csv

total_months = 0
net_total = 0
last_net = 0
increase = 0
max_money = 0
max_date = ""
min_money = 0
min_date = ""
total_change = 0
net_change = 0
nc_list = []
profit = []
date = []

#Join the CSV files
pybank_csv = os.path.join('Resources', 'PyBank.csv')

new_pybank = []
total_profits = []
#Read the CSV files and check to see the types 
with open(pybank_csv) as csvfile:
    #List representation of CSV file
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    firstrow = next(csvreader)
    print(f'CSV Header: {firstrow}')
    print(type(firstrow))

    #Find number of months
    total_months+=1
    
    net_total += int(firstrow[1])
    last_net = int(firstrow[1])
    

    for row in csvreader:
        date.append(row[0])
        profit.append(int(row[1]))
        #Find the net total
        net_total += int(row[1])
        #Find number of months
        total_months+=1
        increase = int(row[1])-last_net
        total_change = total_change + increase
        #Finding net change
        net_change = int(row[1])- last_net
        #Resetting the last net
        last_net = int(row[1])
        nc_list.append(net_change)

        
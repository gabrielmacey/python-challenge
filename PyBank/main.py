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
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    firstrow = next(csvreader)
    print(f'CSV Header: {firstrow}')
    print(type(firstrow))
    total_months+=1
    #List representation of CSV file
    

    net_total += int(firstrow[1])
    last_net = int(firstrow[1])
    #Print out number of months
    #print('Total Months:', total_months)

    #for row in csvreader:
        #date.append(row[0])
        #profit.append(int(row[1]))
        
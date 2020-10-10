import os
import csv

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
    #List representation of CSV file
    pybank = list((csvreader))
    #Find the length of the list and subtract one for header
    total_months = len(pybank)
    #Print out number of months
    print('Total Months:', total_months)

    for row in csvreader:
        date.append(row[0])
        profit.append(int(row[1]))
        
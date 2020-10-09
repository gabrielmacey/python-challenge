import os
import csv

#Join the CSV files
pybank_csv = os.path.join('Resources', 'PyBank.csv')

#Read the CSV files and check to see the types 
with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #List representation of CSV file
    pybank = list((csvreader))

    #Find the length of the list and subtract one for header
    total_months = len(pybank)-1

    #Print out number of months
    print("Total Months:", total_months)

    #Print out the sum of Profit/Losses
    del pybank(0)
    column = 1
    print(sum(row[1] for row in pybank))
    net_total = (pybank[]) #This gives me the first row
    print(net_total)

## total_net = sum()
## print("The total net gain/loss is:", total_net)


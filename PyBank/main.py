import os
import csv

#Join the CSV files
pybank_csv = os.path.join('Resources', 'PyBank.csv')

new_pybank = []
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

    #Print out the sum of Profit/Losses
    Floats = float(pybank['Profit/Losses'])
    #total = sum(float(row["Profit/Losses"]) for row in reader)
    #print("Total: $" + format(str(total))+"0")
import os
import csv

#Join the CSV files
pybank_csv = os.path.join('Resources', 'PyBank.csv')

#Read the CSV files and check to see the types 
with open(pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)
    print(f'CSV Header: {csv_header}')
    print(type(csv_header))

    for row in csvreader:
        print(row)
    
    pybank = list(csvreader)
    



print("The total number of months is:", total_month)

## total_net = sum()
## print("The total net gain/loss is:", total_net)


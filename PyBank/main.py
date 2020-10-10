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

        #Now need to find the max and the min
        if (int(row[1])> max_money):
            max_money = int(net_change)
            max_date = row[0]
        if (int(row[1]) < min_money):
            min_money = int(net_change)
            min_date = row[0]

total_change = round(sum(nc_list)/len(nc_list),2)

pybank_results = (
    f"\n\n Financial Analysis\n"
    f"-----------------------\n"
    f"Total Months: {total_months}\n"
    f"Net Profit: ${net_total}\n"
    f"Average Change: ${total_change}\n"
    f"Greatest Change in Profits: {max_date} ${max_money}\n"
    f"Greatest Change in Losses: {min_date} ${min_money}\n"
)
        
print(pybank_results)

output = os.path.join("..", "Analysis")

with open(output, "w") as csvfyle:

    csvwriter = csv.writer(csvfyle)

    csvfyle.write(pybank_results)
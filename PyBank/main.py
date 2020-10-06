import os
import csv

#Join the CSV files
csv_path = os.path.join('Resources', 'PyBank.csv')

#Read the CSV files and check to see the types
with open(csv_path, 'r') as file_handler:
    bank_data = file_handler.read()
    print(bank_data)
    print(type(bank_data))

#Find the count of months ###########################
total_month = len(bank_data)
print("The total number of months is:", total_month)

# total_net = sum(bank_data[1])
# print(total_net)
import os
import csv

#Join the CSV files
csv_path = os.path.join('Resources', 'PyBank.csv')

#Read the CSV files
with open(csv_path, 'r') as file_handler:
    lines = file_handler.read()
    print(lines)
import os
import csv

#Join the CSV files
csv_path = os.path.join('Resources', 'PyPoll.csv')

#Read the CSV files and check to see the types
with open(csv_path, 'r') as file_handler:
    poll_data = file_handler.read()
    #print(poll_data)

#total_votes = len(poll_data)
#print("Total Votes:", total_votes)


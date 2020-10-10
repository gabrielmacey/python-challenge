import os
import csv

total_votes = 0
candidate = []
candidate_votes = {}
#Join the CSV files
csv_path = os.path.join('Resources', 'PyPoll.csv')

#Read the CSV files and check to see the types
with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidate:
            candidate.append(candidate_name)
            candidate_name = 0
            print(candidate_name)

    for candidate_1 in candidate_votes:
        votes = candidate_votes.get(candidate_1)
        votes_percent = votes/total_votes
        votes_percent = round(votes_percent, 2)
        print(votes_percent)   


election_results = (
    f"\n\n Election Results\n"
    f"-----------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
    f"{candidate_votes}\n"
)
print(election_results,end="")
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
        
        if candidate_name not in candidate_votes:
            candidate_votes[candidate_name] = 0
    
        candidate_votes[candidate_name] += 1

    print("Election Results")
    print("--------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")

    winner = (None, 0)
    for candidate_name in candidate_votes:
        candidate_vote_tally = candidate_votes[candidate_name]
        votes_percent = candidate_vote_tally / total_votes
        votes_percent = "{:.2%}".format(votes_percent)
        if candidate_vote_tally > winner[1]:
            winner = (candidate_name, candidate_vote_tally)
        print(f'{candidate_name}: {votes_percent} {candidate_vote_tally} votes')

    print(f"Winner: {winner[0]}")

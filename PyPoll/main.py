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
            candidate_votes[candidate_name] = 0
            #{"Khan":45}
        candidate_votes[candidate_name] +=1

    for candidate_1 in candidate_votes:
        votes = candidate_votes.get(candidate_1)
        votes_percent = votes/total_votes
        print(votes_percent)   

election_results = (
    f"\n\n Election Results\n"
    f"-----------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)
#print(election_results,end="")
#print(total_votes)
#print(candidate_votes)



#total_votes = len(poll_data)
#print("Total Votes:", total_votes)


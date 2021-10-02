#PyPoll
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote

import os
import csv

#path for CSV

pypollpath = os.path.join("Resources", "PyPoll_Resources_election_data.csv")

count = 0
candidatelist = []
unique_candidate = []
vote_count = []
vote_percent = []

with open(pypollpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
   
    for row in csvreader:
        
        count = count + 1
        
        candidatelist.append(row[2])
        
    for x in set(candidatelist):
        unique_candidate.append(x)
        
        y = candidatelist.count(x)
        vote_count.append(y)
        
        z = (y/count)*100
        vote_percent.append(z)
        
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]
    
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes: " + str(count))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")")
print("-------------------------")
print("Election Winner: " + winner)
print("-------------------------")

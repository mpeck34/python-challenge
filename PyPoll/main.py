# import what we need
import csv
import os

# create dict for incoming data
election_dict = {}

cwd = os.getcwd()
election_data_path = os.path.join("PyPoll","Resources","election_data.csv")

counter = 0 
with open(election_data_path, 'r') as election_data:
    csvreader = csv.reader(election_data, delimiter=",")
    for row in csvreader:
        election_dict[row[0]] = row[2]
        counter += 1

total_votes = len(election_dict)-1

print(total_votes)

stockham_vote = 0
degette_vote = 0
doane_vote = 0

for ballot_id, candidate in election_dict.items():
    if candidate == "Charles Casper Stockham":
        stockham_vote += 1
    elif candidate == "Diana DeGette":
        degette_vote += 1
    elif candidate == "Raymon Anthony Doane":
        doane_vote += 1

print(stockham_vote)
print(degette_vote)
print(doane_vote)

stockham_percent = stockham_vote/total_votes
degette_percent = degette_vote/total_votes
doane_percent = doane_vote/total_votes







    




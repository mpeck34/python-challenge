# import what we need
import csv
import os

# create dict for incoming data
election_dict = {}

# load .csv file
cwd = os.getcwd()
election_data_path = os.path.join("PyPoll","Resources","election_data.csv")

# storing header for some reason
election_dict_header = []

# write .csv file data into a dictionary
counter = 0 
with open(election_data_path, 'r') as election_data:
    csvreader = csv.reader(election_data, delimiter=",")
    for row in csvreader:
        if row[0] == "Ballot ID":
            election_dict_header = [row[0], row[1], row[2]]
            break
    for row in csvreader:
        election_dict[row[0]] = row[2]
        counter += 1

# calc total votes
total_votes = len(election_dict)-1

# create variables to save respective votes
stockham_vote = 0
degette_vote = 0
doane_vote = 0

# iterate and count respective votes
for ballot_id, candidate in election_dict.items():
    if candidate == "Charles Casper Stockham":
        stockham_vote += 1
    elif candidate == "Diana DeGette":
        degette_vote += 1
    elif candidate == "Raymon Anthony Doane":
        doane_vote += 1

# calc percent of votes
stockham_percent = round(((stockham_vote/total_votes) * 100),3)
degette_percent = round(((degette_vote/total_votes) * 100),3)
doane_percent = round(((doane_vote/total_votes) * 100),3)

# compare respective votes and determine winner
def calc_winner(list):
    winner_result = ""
    temp_winner = 0
    for candidate in list: 
        if candidate > temp_winner:
            temp_winner = candidate
    if temp_winner == stockham_vote:
        winner_result = "Charles Casper Stockham"
    elif temp_winner == degette_vote:
        winner_result = "Diana DeGette"
    elif temp_winner == doane_vote:
        winner_result = "Raymon Anthony Doane"
    return winner_result

# save winner
winner_list = [stockham_vote, degette_vote, doane_vote]
winner = calc_winner(winner_list)

# create dashes for interesting appearance
dashes = ""
for i in range(20):
    dashes += "-"

# write results to .txt file
with open(os.path.join("PyPoll", "analysis", "ElectionResults.txt"), "w") as output_text_file:
    output_text_file.write("Election results")
    output_text_file.write("\n\n" + dashes)
    output_text_file.write(f"\n\n Total Votes: {total_votes}")
    output_text_file.write("\n\n" + dashes)
    output_text_file.write(f"\n\n Charles Casper Stockham: {str(stockham_percent)}% ({str(stockham_vote)})")
    output_text_file.write(f"\n\n Diana DeGette: {str(degette_percent)}% ({str(degette_vote)})")
    output_text_file.write(f"\n\n Raymon Anthony Doane: {str(doane_percent)}% ({str(doane_vote)})")
    output_text_file.write("\n\n" + dashes)
    output_text_file.write(f"\n\n Winner: {winner}")
    output_text_file.write("\n\n" + dashes)

# print results in terminal
print("\nElection results")
print("\n" + dashes)
print(f"\n Total Votes: {total_votes}")
print("\n" + dashes)
print(f"\n Charles Casper Stockham: {str(stockham_percent)}% ({str(stockham_vote)})")
print(f"\n Diana DeGette: {str(degette_percent)}% ({str(degette_vote)})")
print(f"\n Raymon Anthony Doane: {str(doane_percent)}% ({str(doane_vote)})")
print("\n" + dashes)
print(f"\n Winner: {winner}")
print("\n" + dashes + "\n")
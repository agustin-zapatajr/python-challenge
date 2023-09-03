# Import dependencies 
import os
import csv

# Set path for file 
csv_path = os.path.join('Resources', 'election_data.csv')

# Initialize variables 
candidate_vote_count = {}
total_votes = 0

# Open file using UTF-8 encoding 
os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(csv_path, encoding='UTF-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)

    # Loop through rows to calculate total votes 
    for row in csv_reader: 
        candidate_name = row[2]
        total_votes += 1
        # Calcuatle total votes per candidate 
        if candidate_name not in candidate_vote_count:
            candidate_vote_count[candidate_name] = 0
        candidate_vote_count[candidate_name] += 1
        total_votes = sum(candidate_vote_count.values())

    # Calculate percentage of votes per candidate 
    candidate_vote_count["Charles Percent"] = round((candidate_vote_count["Charles Casper Stockham"]/total_votes) * 100, 3)
    candidate_vote_count["Diana Percent"] = round((candidate_vote_count["Diana DeGette"]/total_votes) * 100, 3)
    candidate_vote_count["Raymon Percent"] = round((candidate_vote_count["Raymon Anthony Doane"]/total_votes) * 100, 3)

    # Calculate which candidate had the most votes 
    candidate_winner = max(candidate_vote_count, key=candidate_vote_count.get)

# Display results 
print("Election Results\n")
print("-------------------\n")
print("Total Vote: " + str(total_votes) + "\n")
print("-------------------\n")
print("Charles Casper Stockham: " + str(candidate_vote_count["Charles Percent"]) + "% " + str(candidate_vote_count["Charles Casper Stockham"]) + "\n") 
print("Diana DeGette: " + str(candidate_vote_count["Diana Percent"]) + "% " + str(candidate_vote_count["Diana DeGette"]) + "\n") 
print("Raymon Anthony Doane: " + str(candidate_vote_count["Raymon Percent"]) + "% " + str(candidate_vote_count["Raymon Anthony Doane"]) + "\n") 
print("-------------------\n")
print("Winner: " + str(candidate_winner) + "\n")
print("-------------------\n")

# Print to txt file
output_result = os.path.join(".", "analysis", "results.txt")

with open(output_result, "w") as txt_file:
    txt_file.write("Election Results" + "\n")
    txt_file.write("-------------------\n")
    txt_file.write("Total Vote: " + str(total_votes) + "\n")
    txt_file.write("-------------------\n")
    txt_file.write("Charles Casper Stockham: " + str(candidate_vote_count["Charles Percent"]) + "% " + str(candidate_vote_count["Charles Casper Stockham"]) + "\n") 
    txt_file.write("Diana DeGette: " + str(candidate_vote_count["Diana Percent"]) + "% " + str(candidate_vote_count["Diana DeGette"]) + "\n")
    txt_file.write("Raymon Anthony Doane: " + str(candidate_vote_count["Raymon Percent"]) + "% " + str(candidate_vote_count["Raymon Anthony Doane"]) + "\n")
    txt_file.write("-------------------\n")
    txt_file.write("Winner: " + str(candidate_winner) + "\n")
    txt_file.write("-------------------\n")
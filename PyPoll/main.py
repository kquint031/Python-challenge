import csv

csvpath = "../PyPoll/Resources/election_data_v2.csv"
outputpath = "../PyPoll/Analysis/election_analysis.txt"

total_votes = 0
candidates = {}
winner = ""
max_votes = 0

with open(csvpath) as csvfile:
    csvreader = csv.DictReader(csvfile, delimiter=',')
    print(csvreader)    
    csv_header = next(csvreader)
      
    total_votes += 1
    for row in csvreader:
        total_votes += 1
        individual = row['Candidate']
        if individual in candidates:
            candidates[individual] += 1
        else:
            candidates[individual] = 1
     
for individual, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    formatted_percentage = "{:.3f}".format(percentage)
    print(f"{individual}: {formatted_percentage}% ({votes})")
    
    # If statement to find the candidate with max votes
    if votes > max_votes:
        max_votes = votes
        winner = individual

# Generate and append poll output(s)
poll_output = "Election Results\n"
poll_output += "-------------------------\n"
poll_output += f"Total Votes: {total_votes}\n"
poll_output += "-------------------------\n"

for individual, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    formatted_percentage = "{:.3f}".format(percentage)
    poll_output += f"{individual}: {formatted_percentage}% ({votes})\n"

poll_output += "-------------------------\n"
poll_output += f"Winner: {winner}\n"
poll_output += "-------------------------\n"

# Print and output results
print(poll_output)

with open(outputpath, "w") as outputfile:
    outputfile.write(poll_output)
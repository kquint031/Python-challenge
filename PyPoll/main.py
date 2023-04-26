import csv

csvpath = "../PyPoll/Resources/election_data_v2.csv"
outputpath = "../PyPoll/Analysis/election_analysis.txt"
# total = 0
# count_votes = 0
# candidates_votecount = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)    
    csv_header = next(csvreader)
        
    # for row in csvreader:
    #     candidates_list = {rows[2]:rows[0] for rows in csvreader}
    #     candidates_votecount = int(row[0]) 
        
        
    #     for row in csvreader:
    #         total += 1
    #         count_votes += candidates_list + (int(row[0]))
                        
            
poll_output=(f'Election Results\n'
f'-------------------------\n'
f'Total Votes: {total}\n'
f'{candidates_list}: {count_votes}\n'
f'-------------------------')

print(poll_output)

with open(outputpath,"w") as outputfile:
    outputfile.write(poll_output)


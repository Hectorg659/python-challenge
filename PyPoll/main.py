#Import Modules
import os
import csv

#Set CSV Path
csvpath = os.path.join('Resources', 'election_data.csv')
#Set CSV Output path
election_outcome = os.path.join('Analysis', 'election_outcome.txt')

#Open Election Data and read CSV File
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter= ',')
    print(csvreader)

    next(csvreader)

    #Assigned Variables
    total_vote_count = 0
    candidates_choices = []
    candidate_votes = {}
    winning_count = 0
    winning_candidate = ""
    #Loop to find vote count/candidate info
    for row in csvreader:
        
        #Total vote counter
        total_vote_count+= 1

        #Setting candidate info
        candidate_info = row[2]
        #Ifstatement to run when a name appears
        if candidate_info not in candidates_choices:
            candidates_choices.append(candidate_info)
            candidate_votes[candidate_info] = 0

        candidate_votes[candidate_info] = candidate_votes[candidate_info] + 1

#Writing changes to new CSV file with final outcome
with open(election_outcome, 'w') as file:

    file.write("Election Results\n")
    file.write("-----------------------------\n")
    file.write(f"Total Votes: {total_vote_count:,}\n")
    file.write("-----------------------------\n")
    #Printing results to terminal
    print("Election Results\n")
    print("-----------------------------\n")
    print(f"Total Votes: {total_vote_count:,}\n")
    print("-----------------------------\n")

    for candidate_info in candidate_votes:
        votes = candidate_votes[candidate_info]
        vote_percentage = float(votes)/float(total_vote_count)*100
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate_info
        voter_output = f"{candidate_info}: {vote_percentage:.3f}% ({votes})\n"

        print(voter_output)
        

        file.write(voter_output)
        

    winning_output = (f"Winner: {winning_candidate}")
    print("-----------------------------\n")
    file.write("-----------------------------\n")
       
    print(winning_output)

    print("-----------------------------\n")

    file.write(winning_output)
    
    file.write("-----------------------------\n")
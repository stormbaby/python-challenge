
import csv
import os

rel_path = './Resources/election_data.csv'

with open(rel_path) as csvfile:
    cvsreader = csv.reader(csvfile)

    # Initialize a total vote counter.
total_votes = 0
cand_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

candidate = {}
candidates = []


# Read the csv and convert it into a list of dictionaries
candidates = []

with open(rel_path) as poll_data:
    csvreader = csv.reader(poll_data)

    # Read the header
    header = next(csvreader)

    # For each row in the CSV file.
    for row in csvreader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

       
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            candidate_votes.update({candidate_name:0})
            
        

        #add a vote to candidate's votes

        current_votes = candidate_votes[candidate_name] 

        current_votes = candidate_votes[candidate_name] + 1
        candidate_votes[candidate_name] = current_votes
       # print(candidate_votes[candidate_name])


# Save the results to our text file.
with open('analysis/PyPoll_output_data', "w") as txt_file:

    
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:}\n"
        f"-------------------------\n\n")

    print(election_results, end="")

    txt_file.write(election_results)

 
        # results to the terminal.
        
  



 
    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results_txt = (
            f"{candidate_name}: {vote_percentage:.3f}% ({votes:})\n")
        candidate_results_print = (
            f"{candidate_name}: {vote_percentage:.3f}% ({votes:})")

        print(candidate_results_print)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results_txt)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
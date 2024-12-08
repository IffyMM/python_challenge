#Dependencies
import csv
import os

#files to load and output
election_csv=os.path.join("Resources", "election_data.csv")
poll_txt=os.path.join("Analysis", "poll.txt")

#Declare Variables

total_votes=0 #total vote 
percent_votes=[]
candidate_names=[]  #candidates options
candidate_number_votes=[] #candidate votes counters
winning_candidate = ""
winning_count = 0
output=""
# Open and read the csv file
with open(election_csv) as election_data:
    reader = csv.reader(election_data)

# Skip the header row
    header = next(reader)

    for row in reader:
        total_votes+=1
        #print(total_votes)
        candidate_name = row[2]
        if row[2] not in candidate_names:
            candidate_names.append(row[2])
            index= candidate_names.index(row[2])
            candidate_number_votes.append(1)
        else:
            index=candidate_names.index(row[2])
            candidate_number_votes[index]+=1
#calculate percent votes
    for votes in candidate_number_votes:
        percentage=(votes/total_votes)*100
        percentage="%.3f%%" % percentage
        percent_votes.append(percentage)

#getting winner candidate
    winner= max(candidate_number_votes)
    index=candidate_number_votes.index(winner)
    winning_candidate=candidate_names[index]


#print output
election_results=(
f"Election Results\n"
f".........................\n"
f"Total Votes: {total_votes}\n"
f".........................\n"
)
print(election_results)

#output to hold all candidates results
output=""


#iterate each candidate,percent votes, total votes
for i in range(len(candidate_names)):
    output+=f"{candidate_names[i]}:  {str(percent_votes[i])}  ({str(candidate_number_votes[i])})\n"


print(output)

#output for winner
winner_summary=(
f".........................\n"
f"Winner: {winning_candidate}\n"
f"...............................\n"
)
print(winner_summary)

#writing on a txt file
with open(poll_txt, "w") as txt_file:
    txt_file.write(election_results)
    txt_file.write(output)
    txt_file.write(winner_summary)



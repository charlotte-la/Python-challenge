# import modules
import csv
import os

# defining variables
Total_votes=0
votescast=0
totalvotescast=0
candidates=[]
numberwon = {}
percentwon=0
winnername=""
winnervotes=0

# open file
csvpath = "./Resources/election_data.csv"  # path to csv file
csvfile = open(csvpath)  # open csv file
reader = csv.reader(csvfile)
header = next(reader)

#The total number of votes cast
for row in reader:
    Total_votes +=1

    #A complete list of candidates who received votes
    #The total number of votes each candidate won
    if row[2] not in candidates:
        candidates.append(row[2])
        numberwon[row[2]]=0
    numberwon[row[2]]+=1

#The percentage of votes each candidate won
for name in numberwon:
    votes = numberwon[name]
    percentage = votes / Total_votes
    poll = percentage * 100
    print(f"{name}: {poll:.3f}% ({votes})")
    
#The winner of the election based on popular vote.
    if votes > winnervotes: 
        winnervotes = votes
        winnername = name

# print analysis
file_to_save = open("election_analysis.txt", "w")
file_to_save.write(f"Election Results\n")
file_to_save.write(f"-------------------------\n")
file_to_save.write(f"Total Votes: {Total_votes}\n")
file_to_save.write(f"-------------------------\n")

for name in numberwon:
    votes = numberwon[name]
    percentage = votes / Total_votes
    poll = percentage * 100
    file_to_save.write(f"{name}: {poll:.3f}% ({votes})\n")

file_to_save.write(f"-------------------------\n")
file_to_save.write(f"Winner: {winnername}\n")
file_to_save.write(f"-------------------------\n")

file_to_save.close()  # close the text file
csvfile.close()  # close the csv file

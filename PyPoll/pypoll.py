import os
import csv
#Path
path = "Resources/election_data.csv"
# Variables
Candidates =[]
votes_num =[]
percent_votes =[]
total_votes =0
csvfile = open(path)
csvreader = csv.reader(csvfile, delimiter =",")
csv_header = next (csvreader)
#Reading the CSV
for row in csvreader:
    total_votes += 1
    if row[2] not in Candidates:
     Candidates.append(row[2])
     index = Candidates.index(row[2])
     votes_num.append(1)
    else:
       index =Candidates.index(row[2])
       votes_num [index]+=1
# Calculating Percentages
for votes in votes_num:
   percentage =(votes/total_votes)*100
   percentage = "%.3f%%" % percentage
   percent_votes.append(percentage)
#Calculating Winner
winner = max(votes_num)
index = votes_num.index(winner)
winner_cdt = Candidates[index]
#Printing Results
print(f"Election Results")
print(f"----------------------------")
print(f'Total Votes:{str(total_votes)}')
print(f"----------------------------")
for x in range(len(Candidates)):
    print(f"{Candidates[x]}: {str(percent_votes[x])} ({str(votes_num[x])})")
print(f"----------------------------")
print(f"Winner: {winner_cdt}")
print(f"----------------------------")
#Outputting to Election Analysis csv
outputpath = "Resources/election_analysis.csv"
with open(outputpath, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["----------------------------------"])
    csvwriter.writerow([str(f"Total Votes:{str(total_votes)} ")])
    csvwriter.writerow(["----------------------------------"])
    for x in range(len(Candidates)):
        csvwriter.writerow([str(f"{Candidates[x]} {str(percent_votes[x])} ({str(votes_num[x])})")])
    csvwriter.writerow(["----------------------------------"])
    csvwriter.writerow([str(f"Winner:{str(winner_cdt)} ")])
    csvwriter.writerow(["----------------------------------"])
import csv
import sys

filename = "election_data.csv"
outputFile = open("electionResults.txt", "w", newline = '\n')
#sys.stdout = outputFile

candidates = {}
totalVotes = 0
results = []

with open(filename, mode = "r", newline = '') as csv_file:
	
	csv_data = csv.DictReader(csv_file)
	for row in csv_data:
		totalVotes += 1
		if(row["Candidate"] in candidates):
			candidates[row["Candidate"]] = candidates.get(row["Candidate"]) + 1
		else:
			candidates[row["Candidate"]] = 1
csv_file.close()

results.append("Election Results")
results.append("------------------------------------")
results.append("Total Votes :" + str(totalVotes))
results.append("------------------------------------")

#sort by descending values of vote
sortedList = sorted(candidates.items() , reverse=True, key=lambda x: x[1])


for val in sortedList:
	results.append(str(val[0]) + " : " + str(round((val[1]/totalVotes)*100,3)) + "% (" + str(val[1]) + ")")
	
results.append("------------------------------------")

for val in sortedList:
	results.append("Winner : " + str(val[0]))
	break

results.append("------------------------------------")

for r in results:
	print(r)
	outputFile.write(r +" \r\n")

outputFile.close()


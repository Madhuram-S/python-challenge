#Import csv package for reading and writing into files
import csv

# filename to read data from
filename = "election_data.csv"

#file to output the results
outputFile = open("electionResults.txt", "w", newline = '\r\n')

#Declare variables that will be used for calculations
candidates = {}
totalVotes = 0
results = [] # list that will store the results

#open the election data file and read through row by row to count total vote, vote by candidate
with open(filename, mode = "r", newline = '') as csv_file:
	
	# using a dictReader to read the file
	csv_data = csv.DictReader(csv_file)
	for row in csv_data:
		#count total votes
		totalVotes += 1 	

		#count votes per candidate										
		if(row["Candidate"] in candidates):
			candidates[row["Candidate"]] = candidates.get(row["Candidate"]) + 1
		else:
			candidates[row["Candidate"]] = 1
#close file
csv_file.close()

#add all the results to already created list
results.append("Election Results")
results.append("------------------------------------")
results.append("Total Votes :" + str(totalVotes))
results.append("------------------------------------")

#sort by descending values of vote
sortedList = sorted(candidates.items() , reverse=True, key=lambda x: x[1])

# add the candidates, their vote % and total votes they have got into the results list
# the candidates are sorted by greatest to lowest
for val in sortedList:
	results.append(str(val[0]) + " : " + str(round((val[1]/totalVotes)*100,3)) + "% (" + str(val[1]) + ")")
	
results.append("------------------------------------")

#Declare the winner
for val in sortedList:
	results.append("Winner : " + str(val[0]))
	break

results.append("------------------------------------")

#output the results to console and file
for r in results:
	print(r)
	outputFile.write(r +" \r\n")

#close any opened files
outputFile.close()


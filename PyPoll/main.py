#Import csv package for reading and writing into files
import csv
import os

# filename to read data from and file to write the results
dataFile = os.path.join(os.path.dirname(__file__), "election_data.csv")
outputFile = os.path.join(os.path.dirname(__file__),"electionResults.txt")


#Declare variables that will be used for calculations
candidates = {} # a dictionary to store the candidates and votes
totalVotes = 0
results = [] # list that will store text for printing

#open the election data file and read through row by row to count total vote, vote by candidate
with open(dataFile, mode = "r", newline = '') as csv_file:
	
	# using a dictReader to read the file and return a dictionary
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

#sort by descending values of vote each candidate has got
sortedList = sorted(candidates.items() , reverse=True, key=lambda x: x[1])

with open(outputFile, mode = "w", newline="\r\n") as opFile:
	#add all the results to already created list
	results.append("Election Results")
	results.append("------------------------------------")
	results.append(f"Total Votes : {str(totalVotes)}")
	results.append("------------------------------------")
	# add the candidates, their vote % and total votes they have got into the results list
	# the candidates are sorted by greatest to lowest
	for val in sortedList:
		results.append(f"{str(val[0])}  :  {str(round((val[1]/totalVotes)*100,3))}% ({str(val[1])})")
		
	results.append("------------------------------------")

	#Declare the winner
	results.append(f"Winner : {str(sortedList[0][0])}")
	
	results.append("------------------------------------")

	#output the results to console and file
	for r in results:
		print(r)
		opFile.write(r +" \r\n")

#close any opened files
opFile.close()


# This Python script analyzes the records of budget_Data.csv to calculate each of the following:
	# The total number of months included in the dataset
	# The total net amount of "Profit/Losses" over the entire period
	# The average change in "Profit/Losses" between months over the entire period
	# The greatest increase in profits (date and amount) over the entire period
	# The greatest decrease in losses (date and amount) over the entire period

# Import library CSV for reading / writing csv and os lib for file operations
import csv
import os

# Set all variables to default values
line_cnt = total_PL  = first_mnth_PL = last_month_PL = dif_val = 0
max_Increase = min_Increase = 0
max_Inc_month = min_Incr_month = ""

# this dictionary captures all monthly avg changes
avgChng_monthly = {}

# this list captures the output of the analysis
results = []

# Define the data file and output file for results
dataFile = os.path.join(os.path.dirname(__file__), 'budget_data.csv')
outputFile = os.path.join(os.path.dirname(__file__), 'pyBank_Analysis.txt')

# read csv file through a csv.dictreader and store it in a dictionary
with open(dataFile, mode="r") as csv_file:
	
	# Store the csv data into Dictionary using DictReader
	csv_data = csv.DictReader(csv_file)

	# Loop to get Sum of profits/losses, # of months and monthly change of profit/losses
	for row in csv_data:
		# when on the first row after header, capture the first month P&L
		if(line_cnt == 0):
			dif_val = float(row["Profit/Losses"])
		else:
			# calculate monthly P&L difference ie. Feb'10 - Jan'10 difference in P/L
			#store in avgChng_monthly dict
			dif_val = float(row["Profit/Losses"]) - dif_val
			avgChng_monthly[row["Date"]] = dif_val
			dif_val = float(row["Profit/Losses"])
		
		line_cnt += 1
		
		# calculate total Profits/Losses over months
		total_PL += float(row["Profit/Losses"])

csv_file.close() # close the budget_data.csv file

# get the average change in P & L across months 
# the dict avgChng_monthly stores the profit/losses change over months
avg_chng = round(sum(avgChng_monthly.values()) / len(avgChng_monthly),2)

#get greatest increase and decrease in profits - using max() and min()
max_Increase = avgChng_monthly[max(avgChng_monthly, key = avgChng_monthly.get)]
max_Inc_month = max(avgChng_monthly, key = avgChng_monthly.get)

min_Increase = avgChng_monthly[min(avgChng_monthly, key = avgChng_monthly.get)]
min_Incr_month = min(avgChng_monthly, key = avgChng_monthly.get)


# Open the file where the result of analysis should be written in 'write' mode 
with open(outputFile,mode = "w", newline = "\r\n") as opFile:

	# Print and output to file the header for analysis
	results.append("Financial Analysis")
	results.append("----------------------------------------------------------")
		
	# add all the results to resultList
	results.append(f"Total Months : {line_cnt}")
	results.append(f"Total: ${str(round(total_PL))}")

	results.append(f"Average Change: ${str(avg_chng)}")

	results.append(f"Greatest Increase in Profits: {str(max_Inc_month)} (${str(round(max_Increase))})")

	results.append(f"Greatest Decrease in Profits: {str(min_Incr_month)} (${str(round(min_Increase))})")

	# print & output to file all the values calculated
	for r in results:
		print(r)
		opFile.write(r + "\r\n")

# close the ouput file
opFile.close()




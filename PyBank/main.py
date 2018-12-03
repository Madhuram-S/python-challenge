# Import library CSV for reading / writing csv
import csv
import os

# Set all variables to default values
line_cnt = total_PL  = first_mnth_PL = last_month_PL = dif_val = 0
avgChng_monthly = {}
max_Increase = min_Increase = 0
max_Inc_month = min_Incr_month = ""

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
		if(line_cnt == 0):
			dif_val = float(row["Profit/Losses"])
		else:
			dif_val = float(row["Profit/Losses"]) - dif_val
			avgChng_monthly[row["Date"]] = dif_val
			dif_val = float(row["Profit/Losses"])
		
		line_cnt += 1
		
		# calculate total Profits/Losses over months
		total_PL += float(row["Profit/Losses"])

csv_file.close()

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




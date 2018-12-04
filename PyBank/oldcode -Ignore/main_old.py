# Import library CSV for reading / writing csv
import csv

# Set all variables to default values
line_cnt = total_PL  = first_mnth_PL = last_month_PL = 0
grt_Increase = grt_decrease = 0
grt_Inc_month = grt_Decr_month = ""

results = []

# Open the file where the result of analysis should be written in 'write' mode 
outputFile = open("pyBank_Analysis_old.txt",mode = "w", newline = "\r\n")

# Print and output to file the header for analysis
results.append("Financial Analysis")
results.append("----------------------------------------------------------")

# read csv file through a csv.dictreader and store it in a dictionary
with open("budget_data.csv", mode="r") as csv_file:
	
	# Read the total number of lines in the CSV data file
	dataLines = csv_file.readlines()

	#print and output the total months of data available in csv file excl. the header row
	results.append("Total Months:" + " " + str(len(dataLines)-1))

	# reset file pointer to begining of the file
	csv_file.seek(0)

	# Store the csv data into dictReader Dictionary
	csv_data = csv.DictReader(csv_file)

	# Loop to get total profits/losses, first month PL, last month PL, greatest Increase in Profit and greatest decrease in profit
	for row in csv_data:
		if(line_cnt == 0):
			first_mnth_PL = float(row["Profit/Losses"])			
		elif(line_cnt == len(dataLines)-2):
			last_month_PL = float(row["Profit/Losses"])
		
		if(grt_Increase < float(row["Profit/Losses"])):
			grt_Increase = float(row["Profit/Losses"])
			grt_Inc_month = row["Date"]
		
		if(grt_decrease > float(row["Profit/Losses"])):
			grt_decrease = float(row["Profit/Losses"])
			grt_Decr_month = row["Date"]
		
		line_cnt += 1
		
		# calculate total Profits/Losses over months
		total_PL += float(row["Profit/Losses"])

	# get the average change in P & L across months 
	avg_chng = round((last_month_PL - first_mnth_PL) / (line_cnt-1),2)

	
	# add all the results to resultList
	results.append("Total:" + " $" + str(round(total_PL)))
	
	results.append("Average Change:" + " $" + str(avg_chng))

	results.append("Greatest Increase in Profits:" + " " + str(grt_Inc_month) + " " + "($" + str(round(grt_Increase)) + ")")

	results.append("Greatest Decrease in Profits:" + " " + str(grt_Decr_month) + " " + "($" + str(round(grt_decrease)) + ")")

	# print & output to file all the values calculated
	for r in results:
		print(r)
		outputFile.write(r + "\r\n")

	# close the csv and txt files
	outputFile.close()
	csv_file.close()



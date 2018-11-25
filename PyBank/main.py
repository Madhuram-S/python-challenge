# Import library CSV for reading / writing csv
import csv

# Set all variables to default values
line_cnt = total_PL  = first_mnth_PL = last_month_PL = 0
grt_Increase = grt_decrease = 0
grt_Inc_month = grt_Decr_month = ""

# Open the file where the result of analysis should be written in 'write' mode 
outputFile = open("pyBank_Analysis.txt","w")

# Print and output to file the header for analysis
print("Financial Analysis")
outputFile.write("Financial Analysis" + "\n")
print("----------------------------------------------------------")
outputFile.write("----------------------------------------------------------" + "\n")

# read csv file through a csv.dictreader and store it in a dictionary
with open("budget_data.csv", mode="r") as csv_file:
	
	# Read the total number of lines in the CSV data file
	dataLines = csv_file.readlines()

	#print and output the total months of data available in csv file excl. the header row
	print(f"Total Months: {len(dataLines)-1}") 
	outputFile.write("Total Months:" + " " + str(len(dataLines)-1) + "\n")

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
	
	# print & output to file all the values calculated
	print(f"Total: ${round(total_PL)}")
	outputFile.write("Total:" + " $" + str(round(total_PL)) + "\n")
	
	print(f"Average Change : ${avg_chng}")
	outputFile.write("Average Change:" + " $" + str(avg_chng) + "\n")

	print(f"Greatest Increase in Profits: {grt_Inc_month} (${round(grt_Increase)})")
	outputFile.write("Greatest Increase in Profits:" + " " + str(grt_Inc_month) + " " + "($" + str(round(grt_Increase)) + ")" "\n")

	print(f"Greatest Decrease in Profits: {grt_Decr_month} (${round(grt_decrease)})")
	outputFile.write("Greatest Decrease in Profits:" + " " + str(grt_Decr_month) + " " + "($" + str(round(grt_decrease)) + ")" "\n")

	# close the csv and txt files
	outputFile.close()
	csv_file.close()



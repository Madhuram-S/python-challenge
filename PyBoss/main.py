
# Python script to convert old employee format to new employee format 
# The required conversions are as follows:
	# The Name column should be split into separate First Name and Last Name columns.
	# The DOB data should be re-written into MM/DD/YYYY format.
	# The SSN data should be re-written such that the first five numbers are hidden from view.
	# The State data should be re-written as simple two-letter abbreviations.

#import required libraries
import csv
import os
from datetime import datetime

#define function to split string at the space and return a list of first and last name
def splitName(n):
	return n.split(' ',1)

#define function to return masked SSN
# function uses rsplit() to split the ssn by - and returns a masked ssn
def maskSSN(ssn):
	splitSSN = ssn.rsplit("-",1)[1]
	return(f"***-**-{splitSSN}")

#define date conversion function, that take date format as yyyy-mm-dd and converts to mm/dd/yyyy format
def formatDate(dateStr):
	dateval = (datetime.strptime(dateStr , '%Y-%m-%d'))
	return dateval.strftime("%m/%d/%Y")

# US State abbr. lookup dictionary
us_state_abbrev = {'Alabama': 'AL','Alaska': 'AK','Arizona': 'AZ','Arkansas': 'AR',
    'California': 'CA','Colorado': 'CO','Connecticut': 'CT','Delaware': 'DE',
    'Florida': 'FL','Georgia': 'GA','Hawaii': 'HI','Idaho': 'ID','Illinois': 'IL',
    'Indiana': 'IN','Iowa': 'IA','Kansas': 'KS','Kentucky': 'KY','Louisiana': 'LA',
    'Maine': 'ME','Maryland': 'MD','Massachusetts': 'MA','Michigan': 'MI','Minnesota': 'MN',
    'Mississippi': 'MS','Missouri': 'MO','Montana': 'MT','Nebraska': 'NE','Nevada': 'NV',
    'New Hampshire': 'NH','New Jersey': 'NJ','New Mexico': 'NM','New York': 'NY','North Carolina': 'NC',
    'North Dakota': 'ND','Ohio': 'OH','Oklahoma': 'OK','Oregon': 'OR','Pennsylvania': 'PA',
    'Rhode Island': 'RI','South Carolina': 'SC','South Dakota': 'SD','Tennessee': 'TN','Texas': 'TX',
    'Utah': 'UT','Vermont': 'VT','Virginia': 'VA','Washington': 'WA','West Virginia': 'WV',
    'Wisconsin': 'WI','Wyoming': 'WY'}

# filepath for old and new employee data

oldempFile = os.path.join(os.path.dirname(__file__),"employee_data.csv")
newempFile = os.path.join(os.path.dirname(__file__),"new_employee_data.csv")

# open the new employee file in write mode
with open(newempFile, mode = "w", newline= '') as writeCSV:
	
	# define new headers
	new_header = ['Emp ID', 'First Name', 'Last Name', 'DOB','SSN','State']

	# use dictwriter to write into csv
	writeData = csv.DictWriter(writeCSV, delimiter = ",", lineterminator = "\n", fieldnames=new_header)	
	writeData.writeheader()

	#open the old format of the employee file to read and change the emplyee data
	with open(oldempFile, mode = 'r', newline= '') as csvFile:
		empData = csv.DictReader(csvFile, delimiter = ",")

		#for each emp. record, split the name into first and last name, mask the SSN and abbreviate the state
		for row in empData:
			nm = splitName(row["Name"])

			# write each row into the new file
			writeData.writerow({new_header[0] : row["Emp ID"],
					new_header[1] : nm[0],
					new_header[2] : nm[1],
					new_header[3] : formatDate(row["DOB"]),
					new_header[4] : maskSSN(row["SSN"]),
					new_header[5] : us_state_abbrev[row["State"]]
					})
	csvFile.close()
writeCSV.close()

			



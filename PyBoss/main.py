import csv

#define function to split string at the space
def splitName(n):
	return n.split()

#define function to return masked SSN
def maskSSN(ssn):
	splitSSN = ssn.rsplit("-",1)[1]
	return(f"***-**-{splitSSN}")


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

empFile = "employee_data.csv"


with open("new_employee_data.csv", mode = "w", newline= '') as writeCSV:
	
	new_header = ['Emp ID', 'First Name', 'Last Name', 'DOB','SSN','State']

	writeData = csv.DictWriter(writeCSV, delimiter = ",", lineterminator = "\n", fieldnames=new_header)	
	writeData.writeheader()

	with open(empFile, mode = 'r', newline= '') as csvFile:
		empData = csv.DictReader(csvFile, delimiter = ",")

		for row in empData:
			writeData.writerow({new_header[0] : row["Emp ID"],
					new_header[1] : splitName(row["Name"])[0],
					new_header[2] : splitName(row["Name"])[1],
					new_header[3] : row["DOB"],
					new_header[4] : maskSSN(row["SSN"]),
					new_header[5] : us_state_abbrev[row["State"]]
					})
	csvFile.close()
writeCSV.close()

			



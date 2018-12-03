# task is to create a Python script to automate the analysis of any such passage using these metrics. Your script will need to do the following:
# 1. Import a text file filled with a paragraph of your choosing.
# 2. Assess the passage for each of the following:
	# 1. Approximate word count
	# 2. Approximate sentence count
	# 3. Approximate letter count (per word)
	# 4. Average sentence length (in words)

#Import csv package for reading and writing into files
import csv
import os

# filename to read data from and file to write the results
txtFile = os.path.join(os.path.dirname(__file__), "raw_data/paragraph_1.txt")

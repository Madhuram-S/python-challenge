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
import re

wcnt = 0

def wrdCnt(txt):
	return len(txt.split(" "))

txtToAnalyse = ["raw_data/paragraph_1.txt", "raw_data/paragraph_2.txt"]
#txtToAnalyse = ["raw_data/paragraph_2.txt"]

for p in txtToAnalyse:
# filename to read data from and file to write the results
	txtFile = os.path.join(os.path.dirname(__file__), p)

	

	with open(txtFile, "r", newline ='') as fileObj:
		para = fileObj.read()

	fileObj.close()

	# replace whitespace chars
	para1 = re.sub(r'\n\n','', para)	

	#Count # of sentences
	sentences = re.split(r'(?<=[.?!\"]) ?\s*?(?=[A-Z\"])', para1, re.M)
	
	#count word in sentences
	wordCnt = sum([wrdCnt(t) for t in sentences])

	# chrCnt_withSpaces = len(para)
	# spacesCnt = para.count(" ")
	# chrCnt_only = chrCnt_withSpaces - spacesCnt

	# count letters excluding spaces
	chrCnt_only = len(re.sub(r"[\s]", "",para))

	#calculate average letter cnt
	avgLetterCnt = chrCnt_only / wordCnt

	#calculate average word cnt / sentence
	avgSentLen = wordCnt / len(sentences)

	print(f"Paragraph Analysis for paragraph {p} starting as")
	print("\n")
	print(f"{para[0:50]}...")
	print("------------------------------------------------------------------")
	print(f"Approximate word count : {wordCnt}")
	print(f"Approximate Sentence count : {len(sentences)}")
	print(f"Average letter count (per word) : {round(avgLetterCnt,1)}")
	print(f"Average Sentence length : {round(avgSentLen,1)}")
	print("------------------------------------------------------------------")


	






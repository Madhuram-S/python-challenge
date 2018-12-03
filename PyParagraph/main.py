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

#txtToAnalyse = ["raw_data/paragraph_1.txt", "raw_data/paragraph_2.txt"]
txtToAnalyse = ["raw_data/paragraph_2.txt"]

for p in txtToAnalyse:
# filename to read data from and file to write the results
	txtFile = os.path.join(os.path.dirname(__file__), p)

	#para = "Adam Wayne, the conqueror, with his face flung back and his mane like a lion's, stood with his great sword point upwards, the red raiment of his office flapping around him like the red wings of an archangel. And the King saw, he knew not how, something new and overwhelming. The great green trees and the great red robes swung together in the wind. The preposterous masquerade, born of his own mockery, towered over him and embraced the world. This was the normal, this was sanity, this was nature, and he himself, with his rationality, and his detachment and his black frock-coat, he was the exception and the accident a blot of black upon a world of crimson and gold."

	with open(txtFile, "r", newline ='') as fileObj:
		para = fileObj.read()

	fileObj.close()

	# split txt into senences
	sentences = re.split("(?<=[.!?]) +", para, re.M)
	wordCnt = sum([wrdCnt(t) for t in sentences])

	chrCnt_withSpaces = len(para)
	spacesCnt = para.count(" ")

	chrCnt_only = chrCnt_withSpaces - spacesCnt

	avgLetterCnt = chrCnt_only / wordCnt

	avgSentLen = wordCnt / len(sentences)

	print(f"Paragraph Analysis for {p}")
	print("------------------------------------------------------------------")
	print(para)
	print("------------------------------------------------------------------")
	print(f"Approximate word count : {wordCnt}")
	print(f"Approximate Sentence count : {len(sentences)}")
	print(f"Average letter count (per word) : {round(avgLetterCnt,1)}")
	print(f"Average Sentence length : {round(avgSentLen,1)}")
	print("------------------------------------------------------------------")









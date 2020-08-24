#CSV_Open.py
#Created by Carissa Romero
#Date: 10/9/19

import csv #need in order to run csv file
import json 
my_dict = {} #create an empty dictionary
with open("deniro.csv") as infile:
	rdr = csv.reader(infile, skipinitialspace=True) #skipinitialspace - make sure there are not extra "" or \
	next(rdr, None) #skip the heading 
	
	for row in rdr:
		if len(row) > 1: # get rid of out of range error
			my_dict[row[2]] = {"score" : int(row[1]), "year" : row[0]} 
			#store data in dict where the key is the movie title
			#value is dict with two keys, score and year
		

with open("deniro_json.txt","w") as outfile: 
	json.dump(my_dict, outfile, indent=4) #save output dict as a JSON in a file

		
		
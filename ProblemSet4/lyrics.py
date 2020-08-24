#lyrics.py
#Created by: Carissa Romero

import sys
import string


if len(sys.argv) != 2: #usage error message
		print("Usage:python" + sys.argv[0] + " <file name>")

else: #if there is not the above error open the file
	with open(sys.argv[1], 'r') as infile:
		data_dict = {} #create an empty dictionary
		songName = next(infile) #takes the first line of the file which is the song name
		songName = songName.rstrip('\n') #takes of the trailing "\n"
		for line in infile: #reads line by line
			for word in line.split(): #reads word by word
				word = word.lower() #lowercase all the words in dict
			#line = line.lower() # boy and Boy would be the same world 
				word = word.strip(string.punctuation + string.digits) #counts word even if there is punctuaction next to it
				if word: 
					if word in data_dict: 
						data_dict[word] += 1 #if the word is in the dict increase the number
					else:
						data_dict[word] = 1 #if it's not this is the first time we are adding it
	
	keys= list(data_dict.keys())		

	for i, value in enumerate(data_dict.values()):

		data_dict[keys[i]]= {'count': value, 'songs': [songName]} #song names stored in list

	print(data_dict)
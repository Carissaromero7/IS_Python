#second.py 
# read in text file
f = open("caractacus.txt", "r") #opens the file in read mode
text = f.read() # read file data and store it in variable text
f.close() #closes the open file

i = 0
text2 = "" #creates string
#want to delete every other alphanumeric character ..
#while ignoring spaces and punctuation
for char in text: 
	if char.isalnum(): # checks if character is alphanumeric
		if(i % 2) == 0: #checks if it is every second character
#+= adds another value with the variable and assigns the new value to the variable			
			text2 += char 
		i += 1
	else:
    		text2 += char
    		
f = open("trimmed_caractacus.txt", "a") #opens a new the file in append mode 
f.write(text2) #writes the contents of text 2 to the new file
f.close()


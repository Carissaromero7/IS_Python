# second.py
# Written by: Wes Cox for IS485/485
# Oct 3, 2019
# Solution to Question 1 of Programming Problem Set #2
#
# Removes every second alphanumeric character from a text file and saves to a second file

# Read the input text into a variable
text = ""
with open("caractacus.txt") as infile:
	text = infile.read()

# Take a look at a tiny bit of the text
print(text[:10])

# Create a variable to store the modified text, rather than modifying the input text inplace.
cleaned = ""

# Need a flag to remember if we dropped the previous character
second = True

# Iterate through each character in the text
for char in text:
	
	if char.isalnum():
		# Character is a candidate to be dropped

		# Flip the flag variable
		second = not second
		if second:
			# This is the second character, should be dropped, so dont add it to the new string
			continue
	# Build the new string
	cleaned += char

# Take a look at what we changed
print(cleaned[:10])

# Save the output
with open("trimmed_caractacus.txt","w") as outfile:
	outfile.write(cleaned)
# factor.py
# Written by: Wes Cox for IS485/485
# Sept 6, 2019
# Solution to Question 1 of Programming Problem Set #1
#
# Prints out a message for each number between 0 and 100 that is a factor of 
# either 5, 7, or 13

factors = [5, 7, 13]

for number in range(1,101):
	# Start with an empty message
	output_msg = ""

	# Check each factor, in order
	for factor in factors:
		if number%factor == 0:
			if len(output_msg) == 0:
				# First factor, build beginning of output message
				output_msg = str(number) + " is a multiple of " + str(factor)
			else:
				# Additional factor, append to message
				output_msg = output_msg + " and " + str(factor)
	if len(output_msg) > 0:
		# At least one factor was found, finish off and print the message
		output_msg = output_msg + "!"
		print(output_msg)
# perfect.py
# Written by: Wes Cox for IS485/485
# Sept 6, 2019
# Solution to Question 5 of Programming Problem Set #1
#
# Calculate all 3-digit perfect numbers

for number in range(100,1000):
	factors = []
	for factor in range(1,number):
		if number%factor == 0:
			factors.append(factor)

	if sum(factors) == number:
		# Convert each factor to a string before joining it. Converting the list to string
		# causes join() to treat each character individually
		output_msg = " + ".join(map(str,factors))
		output_msg += " = " + str(number)
		print(output_msg)
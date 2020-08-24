# fib.py
# Written by: Wes Cox for IS485/485
# Sept 6, 2019
# Solution to Question 2 of Programming Problem Set #1
#
# Prints out the Fibonacci number corresponding to the index value provided on the command line

import sys

if len(sys.argv) != 2:
	print("Usage: python " + sys.argv[0] + " <index>")
	sys.exit()

n = int(sys.argv[1])

n_1 = 1 # n minus 1 value
n_2 = 0 # n minus 2 value

if n < 0:
	print("Invalid index")
	sys.exit()
elif n <2 :
	# The first two Fibonacci numbers are equal to their index
	print(n)
else:
	index = 1
	# Calculate each Fibonacci number until we reach the required index
	while index < n:

		fib = n_1 + n_2
		
		# Update the previous two fib numbers
		n_2 = n_1
		n_1 = fib

		# Move to next index
		index += 1

	print(fib)

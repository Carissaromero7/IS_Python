# inspector.py
# Written by: Wes Cox for IS485/485
# Sep 26, 2019
# Solution to Question 1 of Programming Problem Set #3
#
# Reads a positive integer from the command line and tests a number of properties

import sys

# Make sure the integer is provided before using it
if len(sys.argv) != 2:
	print("Usage: python " + sys.argv[0] + " <number to be checked>")
	sys.exit()

num = int(sys.argv[1])

# Define all the functions before calling them

def isOdd(n):
	if num % 2 == 0:
		print("The number " + str(n) + " is not odd.")
	else:
		print("The number " + str(n) + " is odd.")

def isSquare(n):
	# Count from 1 to n, and see if any of those numbers square to n.
	# Cleaner than calculating a square root (all integers)
	for i in range(0,n+1):
		# If the square is bigger than n, then we know we have checked all
		# the possibilties and none of them worked
		if i * i > n:
			print("The number " + str(n) + " is not square.")
			return
		elif i * i == n:
			print("The number " + str(n) + " is square.")
			return
	print("The number " + str(n) + " is not square.")

def isIncreasing(n):
	# Convert the integer to a string, so each digit can be treated as a 
	# character in a list
	string = str(n)
	if len(string) < 2:
		# Single digit numbers are defined as increasing
		print("The number " + str(n) + " is increasing.")
		return

	# Iterate through each digit, starting from one past the first
	# Check if this number is not bigger than the previous -> not increasing
	for i in range(1,len(string)):
		if string[i-1] >= string[i]:
			print("The number " + str(n) + " is not increasing.")
			# Short circuit return to stop looking after a violation has been found
			return

	print("The number " + str(n) + " is increasing.")

def isPalindrome(n):
	string = str(n)
	if len(string) < 2:
		print("The number " + str(n) + " is a palindrome.")
		return

	# Start with the first and last indices. Check that they have equal characters.
	# Then move both indices inwards and check they have equal characters. 
	# Repeat until the indices meet.
	start = 0
	stop = len(string) - 1
	while stop - start > 0:
		if string[start] != string[stop]:
			print("The number " + str(n) + " is a not a palindrome.")
			return
		start += 1
		stop -= 1

	print("The number " + str(n) + " is a palindrome.")
	
def isFactorial(n):
	if n == 0:
		print("The number " + str(n) + " is not a factorial.")
		return

	if n < 3:
		print("The number " + str(n) + " is a factorial.")
		return

	product = 1

	# Multiply all the numbers from 1 to n, until either it equals n or exceeds n.
	# Equals means it is a factorial, exceeds means not a factorial.
	for i in range(1,n):
		product = product * i
		if product > n:
			print("The number " + str(n) + " is not a factorial.")
			return
		elif product == n:
			print("The number " + str(n) + " is a factorial.")
			return
	print("The number " + str(n) + " is not a factorial.")
	return

# Call all the tests
isOdd(num)
isSquare(num)
isIncreasing(num)
isPalindrome(num)
isFactorial(num)



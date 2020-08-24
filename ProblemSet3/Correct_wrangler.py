# wrangler.py
# Written by: Wes Cox for IS485/485
# Sep 26, 2019
# Solution to Question 2 of Programming Problem Set #3
#
# Reshape two input words in a predetermined way

import sys

# Make sure both words are provided before using them
if len(sys.argv) != 3:
	print("Usage: python " + sys.argv[0] + " <first word> <second word>")
	sys.exit()

first = sys.argv[1]
second = sys.argv[2]

def spellBackwards(word):
	# Reverse the order of the string
	return word[::-1]

def capitalize(word):
	return word.upper()

def threadTogether(left, right):
	result = ""
	# Increment the index, interspersing the characters from each string.
	# Once the index has exceeded one of the strings, stop adding from it.
	for i in range(0,max(len(left),len(right))):
		if i < len(left):
			result += left[i]

		if i < len(right):
			result += right[i]
	return result

def printOut(f, s, b, c, t):
	# Build the required string from the input parameters
	print("The reverse of {0} is {1}.".format(f, b))
	print("The capital of {0} is {1}.".format(s, c))
	print("Threaded, they become {0}.".format(t))

back = spellBackwards(first)
capital = capitalize(second)
thread = threadTogether(back, capital)

printOut(first, second, back, capital, thread)

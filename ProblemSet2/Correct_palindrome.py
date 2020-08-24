# palindrome.py
# Written by: Wes Cox for IS485/485
# Oct 3, 2019
# Solution to Question 4 of Programming Problem Set #2
#
# Prints out all the 7 digit palindromes

# sqrt(1,000,000) = 1,000
# sqrt(10,000,000) = 3,162.3
# So only need to iterate from 1000 to 3163

for number in range(1000,3163):
	# Only evaluate the square numbers
	candidate = str(number*number)
	if len(candidate) == 7 and \
		candidate[0] == candidate[6] and \
		candidate[1] == candidate[5] and \
		candidate[2] == candidate[4]:
		# A seven digit number only needs to check the outside 3 digits, candidate[3] is irrelevant
		print(candidate + " is a palindrome")
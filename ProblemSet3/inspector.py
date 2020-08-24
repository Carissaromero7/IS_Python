#inspector.py
# Created by: Carissa Romero
# Date: 9/27/19

# Takes a single positive integer as input 
import sys 
#Arguments live in sys.argv
import math
#Need math for square root function

#Make sure the input is a single integer 
#sys.argv = ["inspector.py", 3]
if len(sys.argv) != 2:
	print("Usage:python" + sys.argv[0] + "<first number>")

#Make sure input is a single positive integer
num = int(sys.argv[1])

if num < 0:
	print ("Not a positive interger")
	sys.exit()

#Is the number odd?
def isOdd(a):
#% caluclates the remainder of a division operation.
	if a % 2 == 0: 
	#if a is an even number the result will be 0.
		return "is not odd."
	else:
		return "is odd."

print("The number " + str(num) + " " + str(isOdd(num)))

#Is the number sqaure?
def isSquare(b):
	root = math.sqrt(b)
	if int(root)**2 == b:
		return "is square."
	else:
		return "is not sqaure."

print("The number " + str(num) + " " + str(isSquare(num)))

#Are all the digits in the number in increasing order?
def isIncreasing(n):
  while (n>=0):
    last = n % 10 # gives the right most digit ex. 21 % 10 == 1
    n = int(n / 10)
    prev = n % 10 #gives the digit previous to the last digit
    if last > prev or prev == 0:
        return "is increasing."
    else:
    	return "is not increasing."
     
print("The number " + str(num) + " " + str(isIncreasing(num)))

#Is the number a palindrome?
def isPalindrome(a):
	istring = str(a) #need to convert i to a string
	#use indexing to ensure that "istring" is a palindrome.
	if istring == istring[::-1]: # [::-1] reverses the string
		return "is a palindrome."
	else:
		return "is not a palindrome."

print("The number " + str(num) + " " + str(isPalindrome(num)))

#Is the number a factorial? I.e. 6 is a factorial because 3! = 3 x 2 x 1 = 6.
def isFactorial(n):
	i = f = 1 #create variables
	while f < n: # the factors "f" should be less than "n"
		i += 1 # adds and then iterates over an iterable object appending each element to itself 
		f *= i # multiplies "" f = f * i. So 3 x 2 x 1.
	if f == n: # sum of "f" (3 x 2 x 1). "f" equals original number (6). 
		return "is a factorial." 
	else:
		return "is not a factorial."

print("The number " + str(num) + " " + str(isFactorial(num)))


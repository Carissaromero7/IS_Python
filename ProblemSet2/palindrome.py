#palindrome = a word, phrase, or sequence that reads the same backward as forward.

import math # need to import in order to use sqrt function.
for i in range(1000000,10000000): # Only want 7 digit palindromes
	# want only square palindromes
	root = math.sqrt(i) #get the square root of i 
	if int(root)**2 == i: # "root" squared should equal i
		istring = str(i)  # need to convert i to a string
		#use indexing to ensure that "istring" is a palindrome.
		if istring == istring[::-1]: # [::-1] reverses the string
			print(istring + " is a palindrome")
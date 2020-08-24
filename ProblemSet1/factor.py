# A range between 0 and 100. Remember that python is 0 indexed.
for x in range (0, 101): 
	
# This loop determines whether each x is a multiple of 5 7 or 13.	
# % finds the remainder after division of one number by another.
	if  x%5 ==0 and x%7 == 0 and x%13 == 0: 
		print(str(x) + " is a multiple of 5 and 7 and 13!") 
	elif x%5 == 0 and x%7 == 0:
		print(str(x) + " is a multiple of 5 and 7!")
	elif x%5 == 0 and x%13 == 0:
		print(str(x) + " is a multiple of 5 and 13!")
	elif x%7 == 0 and x%13 == 0:
		print(str(x) + " is a multiple of 7 and 13!")	
	elif x%5 == 0 :
		print(str(x) + " is a multiple of 5!") 
	elif x%7 == 0 :
		print(str(x) + " is a multiple of 7!")	
	elif x%13 == 0 :
		print(str(x) + " is a multiple of 13!")	
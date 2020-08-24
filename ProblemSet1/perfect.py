#python ./perfect.py 

for p in range(100,1000): # You only want 3-digit perfect number(s)
	result = 0
	a= [] #creates a list 
	for i in range (1,p):
		if(p%i) ==0:
			result=result+i
			a.append(i) # adds elements of "i" into my list "a"
	a.sort() # sorts items in my list from ascending order		
	if p==result: #checks if p is a 3-digit perfect number
		#print(p) # p is the perfect number(s) - There is only 1 3-digit perfect #		
		print(' + '.join(str(i) for i in a) + " = " + str(p)) # .join will place a "+" between each item in the list a"
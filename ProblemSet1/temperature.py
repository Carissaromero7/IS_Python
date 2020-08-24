#Conversion from F to C 
# This loop  coverts F (0 to 300 degrees) to C in steps of 20 degrees. 
for F in range (0,301,20):
    
#.= decimal 2f= the amount of decimals (2) and that its is a float (f)
#.format contains the conversion equation
	print(str(F) + "°F = {0:.2f}°C" .format((F-32) * 5/9))
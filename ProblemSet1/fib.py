#Calculating Fibonacci number
#import sys for argv function
import sys

#import math for sqrt function
import math

#Checks input argument validity before use
if len(sys.argv) != 2:
   # print("Not enough arguments")
     print ("Usage: python " + sys.argv[0] + " <first integer>")   
     sys.exit()

# argv = [filename, n]  provide n in the command line 
# Use the int function to convert argv[1] into an integer
firstArg = int(sys.argv[1])

#Use the golden ratio to calculate any Fibonacci number
print(round(((1.61803398875)**firstArg - (-0.61803398875)**firstArg)/math.sqrt(5))) 


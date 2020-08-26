import sys

# argv = [filename, 5, 3]  need to hand the argument (ex. 5) in command line 

if len(sys.argv) != 3:
   # print("Not enough arguments")
     print ("Usage: python " + sys.argv[0] + " <first integer> <second integer>")   
     sys.exit()

firstArg = int(sys.argv[1])
secondArg = int(sys.argv[2])

print(firstArg * secondArg)
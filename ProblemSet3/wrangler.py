#wrangler.py
#Created by: Carissa Romero
#Date: 9/29/19
  
import sys 
#arguments live in sys.argv

#takes two words as input from the command line
#sys.argv = ["wrangler.py", hello, world]
if len(sys.argv) != 3:
	print("Usage:python" + sys.argv[0] + "<first word> <second word>")

first = str(sys.argv[1])
second = str(sys.argv[2])

#Reverse the letters in the first word.
def spellBackwards(a):
	backwards = a[::-1]
	return backwards
#print(spellBackwards(first))


#Capitalize (uppercase) the letters in the second word.
def capitalize(a):
    result = ''
    for char in a:
        if ord(char) >= 65:
            result += chr(ord(char) - 32)
    return result
#print(capitalize(second))


#Thread the two resulting reversed and capitalized words together.
def threadTogether(a, b):
    if not (a and b):
        return a + b
    return a[0] + b[0] + threadTogether(a[1:], b[1:])
#print(threadTogether(spellBackwards(first), capitalize(second)))


#Print everything out.
# need to create this function in order to input the different arguments for each function
def f_default(a): 
	return (a)

#creating the printOut function which switches cases.	
def printOut(case):
    return {
        "a":spellBackwards,
        "b":capitalize,
        "c":threadTogether
    }.get(case, f_default)  
#case = a particular function. f_default = the argument/input for the function 
print ("The reverse of" + " " + str(first) + " " + "is" + " " + printOut("a")(first))  
print ("The capital of" + " " + str(second) + " " + "is" + " " + printOut("b")(second))
print ("Threaded, they become " + printOut("c")(spellBackwards(first), capitalize(second)))




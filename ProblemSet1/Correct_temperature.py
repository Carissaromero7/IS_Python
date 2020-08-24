# temperature.py
# Written by: Wes Cox for IS485/485
# Sept 6, 2019
# Solution to Question 3 of Programming Problem Set #1
#
# Convert fahrenheit temperatures to celsius

for fahr in range(0,301,20):
	celsius = (fahr - 32)*5/9
	print("{0}°F = {1:.2f}°C".format(fahr, celsius))
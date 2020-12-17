''' This program calculates the area of a regular polygon'''
# Import tan and pi from math library
from math import tan, pi

# Request inputs from user
n = int(input("Please enter the number of sides of the polygon: \n"))
s = int(input("Please enter the length of one side of the polygon in meter: \n"))

# Calculate area of the regular polygon
area = (n*(s**2))/(4*tan(pi/n))

# Define the SI unit for area
meter_square = "m\u00b2"

# Print the result
print("The area of the regular polygon is {0:.2f}{1}".format(area, meter_square))
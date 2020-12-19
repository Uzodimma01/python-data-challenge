''' This program reads the value of radius from a user
and uses it to compute the area of a circle and the
volume of a sphere'''

# Import pi from math module
from math import pi

# Define the SI unit for area
meter_square = "m\u00b2"

# Request the value of r from the user
r = float(input("Kindly enter the value of the radius: \n"))

# Calculate the area of a circle
area = pi*(r**2)

# Print the area of a circle
print("The area of the circle is {0:.2f}{1}".format(area, meter_square))

# Calculate the volume of a sphere
volume = (4/3)*pi*(r**3)

# Print the volume of a sphere
print("The volume of the sphere is {0:.2f}{1}".format(volume, meter_square))
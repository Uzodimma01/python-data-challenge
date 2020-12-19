'''This program reads the mass of water and the temperature change
from a user and uses it to compute the total amount of energy
that needs to be added or removed to achieve the desired temperature change
and also compute the cost of heating the water'''

# Request the mass of the water from the user
m = float(input("Please enter the volume of the water to be heated: "))

# Request the temperature change of the water from the user
t = int(input("Please enter the change in temperature of the water to be heated: "))

# Declare the specific heat capacity of water
c = 4.186

# Compute the energy needed to achieve the desired change in temperature
q = m*c*t

# Print the energy needed
print("The energy needed to achieve the desired change in temperature is {0:.2f}j".format(q)) 

# Declare the value Kwh
kwh = (2.77778e-7)*1

# Compute the cost of electricity needed to heat the water
bill = kwh*8.9

# Print the energy needed
print("The cost to boil the water is {0:.2f} cent".format(bill))
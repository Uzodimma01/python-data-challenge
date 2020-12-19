'''This program reads the air temperature in celcius and 
wind speed in km/h and computs the wind chill index'''

# Request the speed of wind from the user in km/h
v = float(input("Please enter the speed of the wind in kilometer per hour, the speed should be up to 4.8 km/h: "))

# Request the air temperature from the user in celcius
t_a = float(input("Please enter the air temperature in celcius, the temperature should be up to 10 degrees: "))

# Compute the wind chill index
wci = (13.12+(0.6215*t_a)) - ((11.37*(v**0.16))+0.3965*t_a*(v**0.16))

# Print the result
if v < 4.8 or t_a < 10:
    print("Invalid wind chill index")
else:
    print("The wind chill index is {}".format(int(wci)))
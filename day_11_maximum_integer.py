'''
This program generates random numbers from 1 to 100, displays each generated number,
indicates the highest number generated as an update and displays the highest generated
number and the number of times the highest number was updated
'''

# Import random
import random

# Create an empty list to hold the list of random numbers generated
random_numbers = []

# Create a list to hold the list of highest numbers generated from
# The list of random numbers. Add 0 to the list so that the list will
# not be an empty list to avoid error when calling max(maximum_numbers) the 
# Initial time
maximum_numbers = [0]

# While random_numbers is less than 100, generate a random number between 1 and 100
# Append the number to random_numbers list
while len(random_numbers) < 100:
    test = random.randrange(1,101)
    random_numbers.append(test)

    # If the number generated is the maximum found in the maximum_numbers list, append 
    # The number to the maximum_numbers list and display <== update beside the number
    if test > max(maximum_numbers):
        maximum_numbers.append(test)
        message = "{} <== update".format(max(maximum_numbers))
    
    # If not, print only the number
    else:
        message = test
    print(message)

# Name a variable that holds the value of the length of maximum_numbers list
# 1 is subtracted from the length of maximum_numbers list to cancel the initial number 0
# That was added in the maximum_numbers list that was not generated
update = len(maximum_numbers)-1

# Display the appropriate meaasge
print("The maximum value found was {}".format(max(random_numbers)))
print("The maximum value was updated {} times".format(update))

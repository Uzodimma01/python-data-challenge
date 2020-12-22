# Import the random module
import random
'''This program simulates a spin in roulette wheel by usin Python's number generator
and displays the number that was selected and all the bets that mus be payed'''

# Create a list to hold the numbers contained in different colors
# Make the numbers a string to differentiate between 0 and 00
red = ["1","3","5","7","9","12","14","16","18","19","21","23","25","27","30","32","34","36"]
black = ["2","4","6","8","10","11","13","15","17","20","22","24","26","28","29","31","33","35"]
green = ["0","00"]

# Create a pool from where the random number will be selected
spin_pool = ["1","3","5","7","9","12","14","16","18","19","21","23","25","27","30","32","34",\
    "36","2","4","6","8","10","11","13","15","17","20","22","24","26","28","29","31","33","35","0","00"]

# Select a random number from the pool
spin = random.choice(spin_pool)

# Typecast the str spin to int and check whether even or odd
even = int(spin)%2 == 0 

# Check for color to pay
if spin in red:
    color = "Pay Red"
elif spin in black:
    color = "Pay Black"
else:
    color = "Pay Green"

# Check whether to pay even or odd
if even and spin not in green:
    is_even = "Pay Even"
elif not even and spin not in green:
    is_even = "Pay Odd"

# Check for range of number to pay
if int(spin) >= 1 and int(spin) <= 18:
    num_range = "Pay 1 to 18"
else:
    num_range = "Pay 19 to 36"

# Display all bets to be payed
if spin in green:
    print("The spin resulted in {}...\nPay {}".format(spin,spin))
else:
    print("The spin resulted in {}...\nPay {}\n{}\n{}\n{}\n".format(spin,spin,color,is_even,num_range))

'''This program reads input from a user and displays a message
indicating whether the input is even or odd number'''

# Request input from the user
num = int(input("Please enter an integer: "))

# Check whether the number is even or odd
## An even number is divisible by 2 with no remainder
if num % 2 == 0:
    message = "This integer is an even integer"
else:
    message = "This integer is an odd integer"

# Print the message
print(message)
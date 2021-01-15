'''
This program asks the user for an integer and converts it to 
decimal'''

# Ask the user for input
digit = int(input("Please enter the number to be converted to decimal: "))

# Assing the digit entered by the user to initial_digit for later use
initial_digit = digit

# Name an empty string for later use
binary = ""

# Name variable with the vallue of 0
integer_part = 0

while digit > 0:
    integer_part = digit//2

    # Assign the remainder of the division to digit_remainder
    digit_remainder = digit % 2

    # Add the remainder to the beginning of binary
    # This does the backward counting when counting the binary answer
    binary = str(digit_remainder) + binary

    # Update the value of digit after each division 
    digit = integer_part
# Display the result
if binary == "":
    print("{} has no binary equivalent".format(initial_digit))
else:
    print("The binary equivalent of {} is {}".format(initial_digit, binary))
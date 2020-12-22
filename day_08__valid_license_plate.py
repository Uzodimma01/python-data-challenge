'''This program accepts input from the user and displays a message
indicating whether the in put is a valid older style license plate
or a newer style license plate'''

# Request input from the user
license_num = input("Please enter a valid license number: ")

# Check whether the license number is an older style license plate
# An older style license plate consists of three uppercase letters followed by three numbers
if license_num[0:3].isalpha() and license_num[0:3].isupper() and len(license_num) == 6 and license_num[3:].isdigit():
    # Indicate that this is an older style license plate
    message = "This is an older style license plate"

# Check whether the license number is an newer style license plate
# A newer style license plate consists of four numbers followed by four uppercase letters
elif license_num[4:].isalpha() and license_num[4:].isupper() and len(license_num) == 7 and license_num[0:4].isdigit():
    # Indicate that this is a newer style license plate
    message = "This is a newer style license plate"

else:
    # Indicate that the input is an invalid one
    message = "The input is not a valid license plate"

# Display the result
print(message)

'''This program reads a letter of the alphabet from the user and 
and displays a message indicating whether the input is a vowel or not'''

# Request input from the user
letter = str(input("Please enter an integer: ")).lower()

# Check whether the letter is a vowel or consonant
## An vowel letter can be A,E,I or U
if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
    message = "This letter is a vowel"
elif letter == 'y':
    message = "Y sometimes is a vowel"
else:
    message = "This letter is a consonant"

# Print the message
print(message)
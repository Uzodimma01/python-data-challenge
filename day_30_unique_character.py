'''
This program prints the number of unique characters in a string that the user enters
'''
# Request input from the user 
word = input("Please enter a word: ")

# Force word to a lower case to avoid duplicate 
# Between an uppercase and lowercase letter
string = word.lower()

# Create an empty dictionary to store the keys and its values
liste = {}

# Iterate through string
for character in string:
    if character in liste:

        # Increase the value of the key by 1
        liste[character]+=1
    else:

        # Add the key to the dictionary and assign it a value of 1
        liste[character]=1

# Display the number of unique characters in the word                  
print("{} has {} unique characters".format(word, len(liste)))


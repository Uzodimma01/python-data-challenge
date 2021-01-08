'''
This program accepts a list of words from the user and returns the list removing
duplicates if any
'''

# Define the function
def no_duplicate():
    '''This function removes duplicate words from the list of words entered by the user'''

    # Request for words from the user
    words = input("Please enter a word, enter a blank line to quit: ").lstrip(" ").rstrip(" ").capitalize()

    # Initialise an empty list to store the list of words
    list_of_words = []

    # Check if the user entered a blank line
    while words != "":

        # Check if the word does not already exists
        if words not in list_of_words:

           # Add the word to the list of words 
           list_of_words.append(words)

        # Request for words from the user
        words = input("Please enter a word, enter a blank line to quit: ").lstrip(" ").rstrip(" ").capitalize()

        # Check if the user entered a blank line
        if words == "":
            
            # Iterate thtough the list of words
            for word in list_of_words:

                # Print each word
                print(word)

# Call the function
no_duplicate()
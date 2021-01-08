'''This program reads a list of numbers from the user, removes the
two largest and smallest values from a list of numbers and returns
the list of numbers and the list of numbers with outliers removed
'''

# Define the function
def remove_outliers():
    '''This function requests a list of numbers from the user and
    removes the two largest and smallest values from a list of numbers'''

    # Request input from user
    list_from_user = input("Please enter a list of numbers: ").strip(" ")

    # Initialise an empty list to store the list of numbers
    list_of_numbers = []
    initial_list = []

    # Check for when the user enters a blank line
    while list_from_user !="":

        # Convert the input to float 
        convert_list_from_user = float(list_from_user)

        # Add the input to the list of numbers
        list_of_numbers.append(convert_list_from_user)
        initial_list.append(convert_list_from_user)

        # Request input from user
        list_from_user = input("Please enter a list of numbers: ").strip(" ")

        # Check for when the user enters a blank line
        if list_from_user == "":

            # Check if the number of inputs is less than 4
            if len(list_of_numbers) < 4:

                # Display an error message
                print("The list of numbers should be more than 4, please try again")
            else:

                # Sort the list of numbers in ascending order
                list_of_numbers.sort()

                # Remove the first two numbers i.e the two smallest numbers
                del list_of_numbers[:2]

                # Remove the last two numbers i.e the two largest numbers
                del list_of_numbers[-2:]

                # Print the initial list and the modified list
                print("The new list without the outliers is", list_of_numbers)
                print("The list of numbers you entered is",initial_list)
            break
    else:

        # Display an error message
        print("The list of numbers should not be empty, please try again")

# Call the function
remove_outliers()
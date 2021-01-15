'''
This program accepts a string of characters from the user,  and displays
whether the string is a valid integer or not
'''

def is_integer(string):
    '''This function accepts as input a string of characters and displays
    whether the string is a valid integer or not
    '''

    # If the first character in string is + or -
    # ommit the first character, an integer can be positive or negative
    if string[0] == "+" or string[0] == "-":
        string = string[1:]

    # If the string entered can be converted to number,
    # Indicate it is a valid integer
    if string.isnumeric():
        print("This is a valid integer")
    else:
        print("This is not a valid integer")


# accept input from the user and strip leading and/or trailing spaces
string = input("Please enter a string: ").strip(" ")

# Call the is_integer function
is_integer(string)
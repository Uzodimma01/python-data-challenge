'''
This program accepts a number from the user, checks if the number is a prime number
and returns either True or False equivalent
'''

def is_prime(number):
    '''
    This function check if a number is a prime number and return the boolean
    equivalent
    '''

    # Name an empty list for later use 
    is_prime_list = []

    # Name an empty string for later use
    is_prime_number = ""

    # Iterate over the range of the number starting from 2 because the first prime number is 2
    # The number itself is not inclusive because if divided by 1 and itself gives no remainder
    for i in range(2, number):

        # Check if the number has no remainder when divided by i and append
        # "This is not a prime number" to the is_prime_number list
        if number % i == 0:
            print(i)
            is_prime_list.append("This is not a prime number")

        # If not, append "This is a prime number" to the is_prime_number list
        else:
            is_prime_list.append("This is a prime number")

    # If is_prime_number list is not empty and "This is not a prime number"
    # Is not in the list, then the number is a prime number
    if len(is_prime_list) != 0 and "This is not a prime number" not in is_prime_list:
        is_prime_number = True

    else:
        is_prime_number = False
    
    # Return the value of is_prime_number as the return value of the function is_prime
    return is_prime_number


# Request a number from the user
number = int(input("Please enter a number to check if it is prime: "))

# Display the returned value of the is_prime function
print(is_prime(number))


def lowest_term(numerator, denominator):
    '''
    This functiontakes in numerator and denominator as fraction and returns the lowest term
    '''

    # Find the lowest number between the numerator and denominator
    lowest = min(numerator, denominator)

    # Name variable new_numerator and nuw_denominator for later use
    new_numerator = 0
    new_denominator = 0


    # Iterate over the lowest number starting from 1 to the lowest number
    for i in range(1, lowest + 1):
        while lowest > 0 and i <= lowest:

            # Reduce the numerator and the denominator if both are divisible by the value
            # Wit no remainder then increase the values of i by 1
            if numerator % i == 0 and denominator % i == 0:
                new_numerator = numerator // i
                new_denominator = denominator // i
            i += 1

    # Return the lowest terms
    return new_numerator, new_denominator
# Request for input for numerator and denominator
numerator = int(input("Please enter the numerator: "))
denominator = int(input("Please enter the denominator: "))

# Check if numerator or denominator is less than 1 and display an error message
if numerator < 1 or denominator < 1:
    print("Invalid entry")

else:
    # Call the lowest_term function and assign the returned values to new_numerator and new_denominator
    new_numerator, new_denominator = lowest_term(numerator, denominator)
    print(str(new_numerator)+" and "+str(new_denominator))
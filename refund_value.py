#In many jurisdictions a small deposit is added to drink containers to encourage people
#to recycle them. In one particular jurisdiction, drink containers holding one liter or
#less have a $0.10 deposit, and drink containers holding more than one liter have a
#$0.25 deposit.
#Write a program that reads the number of containers of each size from the user.
#Your program should continue by computing and displaying the refund that will be
#received for returning those containers. Format the output so that it includes a dollar
#sign and always displays exactly two decimal places.

num_bottles_returned = int(input("Please enter the number of bottles you wish to return: \n")) # Ask user to enter the number of bottle to return
# and assign it to num_bottles_returned variable
bottles_remain = num_bottles_returned
value_of_container = [] # A list to hold the values of value_of_container
print("Hello there, in this jurisdiction, drink containers holding one liter or \
less have a $0.10 deposit, and drink containers holding more than one liter have a $0.25 deposit.")
while bottles_remain > 0:
    returned = bottles_remain
    bottles = int(input("Please press 1 if container {} holds one liter or less, else press 2: \n".format(returned))) # Request the
    # user to enter the number corresponding to the size of the container and assign it to bottles variable
    if bottles == 1:
        value = 0.10 # Assign the value of 0.10 for containers holding one liter or less to the value variable
    elif bottles == 2:
        value = 0.25 # Assign the value of 0.25 for containers holding more than one liter value variable
    else:
        while bottles != 1 or bottles != 2:
            print("Invalid input, kindly make a valid input") # Notify the user of invalid input made and end the program
            break
        break
    bottles_remain -= 1 # Decrease bottles_remain by 1
    value_of_container.append(value) # Append the value of the container to the value_of_container list
total = sum(value_of_container) # Sum the values in value_of_container and assing it to value variable
print("----------------------------------------------------------------------------------------------------------------------------------------")
print("Hello there, the refund for the {0} bottles is ${1:.2f}".format(num_bottles_returned, total))
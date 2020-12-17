'''This program reads a positive integer from the user 
and then displays the sum of all the integers from 1 to n'''

# Request input from user for the value of n
n = int(input("Please enter a positive integer: \n"))

# Calculate the sum of the integers
ans = (n*(n+1))/2

# Print the result
print("The sum of the integer is " + str(ans))
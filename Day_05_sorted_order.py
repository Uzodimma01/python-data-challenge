'''This program accepts three integers from the user
and display them in sorted order from the smallest to
the largest'''

# Read input from the user
num_1 = int(input("Please enter the first number:"))
num_2 = int(input("Please enter the second number:"))
num_3 = int(input("Please enter the third number:"))

# Sort the numbers
smallest_num = min(num_1,num_2,num_3)
largest_num = max(num_1,num_2,num_3)
middle_num = (num_1 + num_2 + num_3) - (smallest_num + largest_num)
print("The smallest number is {0}, the middle number is {1}, the largest number is {2}".format(smallest_num,middle_num,largest_num))
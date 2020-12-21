'''This program reads the lengths of 3 sides of a triangle from the user 
and displays a message indicating the type of the triangle'''

# Request the lengths of the triangle from the user
side_a = float(input("Please enter the length of side a of the triangle: "))
side_b = float(input("Please enter the length of side b of the triangle: "))
side_c = float(input("Please enter the length of side c of the triangle: "))

# Check the type of the triangle using the lenght of sides
if side_a == side_b and side_b == side_c:
    message = "This is an equilateral triangle because all sides have equal lengths"
elif side_a != side_b and side_b != side_c:
    message = "This is a scelene triangle because all sides is different lengths"
else:
    message = "This is an isosceles triangle because two sides have equal lenghts"

# Display the type of triangle
print(message)
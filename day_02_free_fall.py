'''Compute the speed of an object when it hits the ground after being dropped
Ignore initial velocity since initial velocity is 0
(To do this, you need to import squareroot from math library)'''
#your code goes here
from math import sqrt
'''Define a constant for the acceleration due to gravity in m/s**2
(For example: Gravity is 9.8)'''
#your code goes here
gravity = 9.8
'''Read the height from which the object is dropped (from the user)'''
#your code goes here
fall_height = int(input("Please enter the height in meter from which the object falls: \n"))
'''Compute the final velocity'''
#your code goes here
accel_due_to_gravity = sqrt(2*gravity*fall_height)
'''Define meter per second in symbol'''
#Your code goes here
meter_per_sec = "m/s\u00b2"
''' Display the result'''
#your code goes here
print("The speed at which the object falls is {0:.2f} {1}".format(accel_due_to_gravity,meter_per_sec))

 
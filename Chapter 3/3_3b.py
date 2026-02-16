# the if-else statement is the most common 
# type of selection statement. 
# It is also called a 2-way selection statement.
import math 

area = float(input("Enter the area: "))

if area > 0: 
    radius = math.sqrt(area / math.pi)
    print("The radius is: ", radius)
else: 
    print("Error: the area must be a positive number")



# print the maximum and minimum of txo input numbers
first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

if first > second: 
    maximum = first
    minimum = second
else: 
    maximum = second
    minimum = first
print("Maximum: ", maximum)
print("Minimum: ", minimum)

# Multi way selection statement 
# can check if they are equal 

first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))

if first > second: 
    maximum = first
    minimum = second
    print("Maximum: ", maximum)
    print("Minimum: ", minimum)
elif: 
    maximum = second
    minimum = first
    print("Maximum: ", maximum)
    print("Minimum: ", minimum)
else: 
    print("These numbers are equal")
    
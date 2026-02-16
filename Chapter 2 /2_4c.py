# you must use a type conversion function 
# when working with the input of numbers 
print(int("33"))
print(float("3.14"))
print(float(33))

# note that the int function covers a float 
# to an int by truncation, not by rounding 
print(int(6.75))

# to round a float to the nearest integer, use a round function
print(round(6.75))

# you can convert a number to a string using the str function 
# Note that python is a strongly typed programming language 
# which means the interpreter checks the types of the value before 
# performing operations on them
profit = 1000.55
print("$" +  str(profit))




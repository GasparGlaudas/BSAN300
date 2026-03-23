# object identity - if two variables refer to the exact same object in memory. 
# Python's is operator can be used to test for object identity

first = [20, 30, 40]
second = first 
third = list(first)

print(first == second)  # object identity (output: true)
print(first == third)  # structural equivalence (output : true)

print(first is second)  # output : true 
print (first is third)  # output : false
# extend performs a similar operation, but adds 
# the elements of its list argument to the end of the list 
example = [1, 2, 3]
example.extend([11, 12, 13])
print(example) # output: [1, 2, 3, 11, 12, 13]

# the method pop is used to remove an element at a given position
example.pop() # remove the last element
print(example) # output: [1, 2, 3, 11, 12]

example.pop(0) # remove the first element 
print(example) # output: [2, 3, 11, 12]

# the method remove is used to remove an element using its value 
example.remove(11)
print(example) # output: [2, 3, 11]




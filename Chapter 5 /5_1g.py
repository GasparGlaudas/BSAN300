"""
The list type includes several methods for 
inserting and removing elements 
The method insert expects an integer index 
and the new elements has arguments 
"""
example = [1, 2]
example.insert(1, 10)
print(example) # [1, 10, 2]

example.insert(3, 25)
print(example) # [1, 10, 2, 25]

# append expects a new element as an argument 
# and adds it to the end of the list

example = [1, 2]
example.append(3)
print(example) # output: [1, 2, 3]
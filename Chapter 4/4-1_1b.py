# the subscript operator, [], allows access to a single character 
# in a string at a given position
name = "Alan Turing"
print(name[0])                 # examine the first character
print(name[3])                 # examine the fourth character
# print(name[len(name)])       # Oops! an index error 
print(name[len(name) - 1])     # Examine the last character
print(name[-1])                # Shorthand for the last character
print(name[-2])                # Shorthand for next to last character

# the string is an immutable data structure - the characters can be 
# accessed but cannot be replaced, inserted, or removed
# name=[0] = "a"                 # Oops!  A type error!

nameList = list(name)
print(nameList)
nameList[0] = "a"
print(nameList)
name = "".join(nameList)
print(name)

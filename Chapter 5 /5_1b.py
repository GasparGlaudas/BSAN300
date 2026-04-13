# It is interesting that when the Python interpreter 
# evaluates a list literal, 
# each of the elements is evaluated as well.

import math
x = 2

print([x, math.sqrt(x)])    # Output: [2, 1.4142135623730951]
print([x + 1])  # Output: [3]

# Lists of integers can be built using the range and list functions

first = [1, 2, 3, 4]
second = list(range(1, 5))
print(first)    # Output: [1, 2, 3, 4]
print(second)   # Output: [1, 2, 3, 4]

# The list function can build a list from any iterable 
# sequence of elements

third = list("Hi there!")
print(third)
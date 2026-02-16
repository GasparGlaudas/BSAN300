# compound boolean expressions 
# often a course of actions must be taken 
# if either of two conditions is true.

# the or operator requires only one of the conditions to be true.

number = int(input("Enter the numeric grade: "))

if number > 100 or number < 0:
    print("Error: grade must be between O and 100")
else: 
    if number > 89:
        letter = "A"
    elif number > 79:
        letter = "B"
    elif number > 69: 
        letter = "C"
    else:
        letter = "F"

    print("The letter grade is", letter)

# The and operator requires both conditions to be true 
number = int(input("Enter the numeric grade: "))

if number <= 100 and number >= 0:
    if number > 89:
        letter = "A"
    elif number > 79:
        letter = "B"
    elif number > 69: 
        letter = "C"
    else:
        letter = "F"
    print("The letter grade is", letter)
else: 
    print("Error: grade must be between O and 100")
    

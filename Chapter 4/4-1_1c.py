# the subscript operator is also useful in loops where you want 
# to use the position as well as the character in a string 
data = "Hi there!"

for index in range(len(data)): 
    print(index, data[index])
    

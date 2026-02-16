# the while loop can be complicated to write correctly; 
# it is possible to simplify it's structure and improve its readability 

theSum = 0

while True: 
    data = input("Enter a number or just enter to quit: ")
    if data == "": 
        break 
    numner = float(data)
    theSum += number 
print("The sum is", theSum)


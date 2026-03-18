"""
String representations of integers and floating-point
numbers can be converted to the numbers by using the 
fonction int and float. 
"""

f = open("integers.txt", "r")
theSum = 0
for line in f:
    line = line.strip()
    number = int(line)
    theSum += number
print("The sum is", theSum)
f.close()



# the next code segment modifies the previous example
# to hande integers separated by spaces and/or newlines 

f = open("integers.txt", "r")
theSum = 0
# for line in f:
    wordlist = lines.split()
    for word in wordlist: 
        number = int(word)
        theSum += number


f.close()

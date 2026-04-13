# example: finding the mode of a list of values 
# the mode of a list of values is the value that occurs most frequently.
# the following script inputs a list of words from a text file and prints their mode. 

fileName = input("Enter the filename: ")
f = open(fileName, "r")

# input the text, convert its words to uppercase, add the words to a list.
upperWords = []
for line in f: 
    words = line.split()
    for word in words: 
        word = word.upper()
        upperWords.append(word)

# obtain unique words and frequencies, saving these to a dictionnary.


# print(upperWords)

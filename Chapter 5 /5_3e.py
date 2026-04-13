# to print all of the keys and their values: 

info = {"name":"Sandy", "occupation":"manager"}

for key in info:
    print(key, info[key])

# alternative: use the dictionnary method items ()
print(list(info.items()))

# access the key and value of each entry in the list withiin a for loop 
for (key, value) in info.items: 
    print(key, value)
    


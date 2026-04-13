# you can sort the list first the traverse it to print 
# the entries of the dictionnary in alphabetical order:

info = {"name":"Sandy", "occupation":"manager"}

theKeys = list(info.keys())
theKeys.sort()

for key in theKeys: 
    print(key, info[key])
    

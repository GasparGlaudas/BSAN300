# python's subscript operator can be used to obtain a substring through 
# a process called slicing by placing a color (:) in the subscript
name = "myfile.txt"

print(name[0:])              # the entire string 
print(name[0:1])             # the first character 
print(name[0:2])             # the first two character 
print(name[:len(name)])      # the entire string 
print(name[-3:])             # the last three character 
print(name[2:6])             # Dril to extract "file"


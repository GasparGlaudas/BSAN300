# in determines an element presence or abscence 

aList = [34, 45, 67]
target = 45

if target in aList: 
    print(aList.index(target))
else: 
    print(-1)

# the method sort mutates a lsit by arranging 
# its elemetns in ascending order 

example = [4, 2, 10, 8]
example.sort()
print(example)  # [2, 4, 8, 10]

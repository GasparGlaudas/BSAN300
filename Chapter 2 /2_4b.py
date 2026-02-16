# ** has the highest precedence and is evaluated first 
print(2 * 3 ** 2)

# Unary negation is evaluated next, before multiplication, division, and remainder 
print(-3 * 2)

# *, /, and % are evaluated before + and -
print(4 + 6 * 2)
print(6 / 2 + 10)
print(7 % 3 + 2)

# + and - are evaluated before =
x = 3 + 4 - 2 

# With two exceptions, operations of equal precedence are left 
# associative so their are evaluated from left to right 
# ** and = are right associative 
print(4 - 2 + 6)
print(20 / 5 * 2)

# You can use parantheses to change the orer of evaluation 
print((4 + 6) * 2) 
print(6 / (2 + 4))



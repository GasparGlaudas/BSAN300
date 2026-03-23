# a tuple resembles a list, but is immutable
# you indicate a tuple by enclosing it's elements in parantheses ()
fruits = ("apple", "banana")
print(fruits)
meats = ("fish", "poultry")
print(meats)

food = meats + fruits
print(food)

veggies = ["celery", "beans"]
print(tuple(veggies))

# f-string (recommended, modern)
name = "Alice"
age = 25
print(f"My name is {name} and I am {age} years old.")

# .format() method (older)
print("My name is {} and I am {} years old.".format(name, age))

# % formatting (very old, like C)
print("My name is %s and I am %d years old." % (name, age))

# in f strings, you can even use math operations
print(f"Next year I will be {age + 1} years old.")

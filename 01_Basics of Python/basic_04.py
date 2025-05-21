# Simple function
def greet():
    print("Hello, World!")

greet()

# Function with parameters
def add(x, y):
    return x + y

result = add(3, 5)
print("Sum:", result)

# Default parameters
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet("John")
greet()

# Keyword arguments
def student_info(name, age):
    print(f"Name: {name}, Age: {age}")

student_info(age=20, name="Alice")

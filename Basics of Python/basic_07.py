# Basic try-except
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("You cannot divide by zero!")
except ValueError:
    print("Please enter a valid number.")
finally:
    print("This block always runs.")

print("Program continues...")

# For loop over a list
names = ["Alice", "Bob", "Charlie"]

for name in names:
    print(name)

# For loop with range
for i in range(5):  # 0,1,2,3,4
    print(i)

# While loop
count = 0

while count < 5:
    print("Count is:", count)
    count += 1

# break and continue
for i in range(10):
    if i == 5:
        break   # Stop the loop when i is 5
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)  # Will print only odd numbers < 5

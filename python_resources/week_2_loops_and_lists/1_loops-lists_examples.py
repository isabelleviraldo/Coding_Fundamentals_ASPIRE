# While Loops
# While loops repeat until a condition is no longer True
count = 5
while count > 0:                # while the count is greater than 0, keep looping
    print("Counting down:", count)
    count = count - 1           # reduce count by 1 each time
print("Blast off!")

# Be careful! If you never update your variable, you can create an infinite loop.
# Example (DONT RUN): while True: print("uh oh")


# For Loops
# For loops are usually better when you know how many times to loop
for i in range(5):              # range(5) gives 0,1,2,3,4
    print("i is:", i)

# You can change the start and step of a range
for i in range(2, 11, 2):       # start at 2, go up to 11, step by 2
    print("Even number:", i)


# Lists
# Lists store multiple items in one variable
numbers = [10, 20, 30, 40, 50]      # a list of integers
names = ["Alice", "Bob", "Charlie"] # a list of strings

# Access by index (starts at 0!)
print(numbers[0])   # 10
print(names[2])     # Charlie

# You can loop through lists easily
for num in numbers:
    print("Number in list:", num)

for person in names:
    print("Hello", person)

# Adding to a list
numbers.append(60)
print(numbers)

# Removing from a list
names.remove("Bob")
print(names)


# Combining Loops and lists
# find the sum of numbers in a list
total = 0
for num in numbers:
    total = total + num
print("The total is:", total)

# while loop through a list using an index
index = 0
while index < len(names):
    print("At index", index, "we have", names[index])
    index = index + 1


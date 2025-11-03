# Bubble Sort Demo
# ----------------
# This program shows how a computer can sort a list of numbers by
# repeatedly comparing and swapping neighboring items.

# Our unsorted list (array)
numbers = [5, 2, 9, 1, 5, 6]

print("Original list:", numbers)

# Bubble sort algorithm
# We’ll use two loops:
# - Outer loop: repeats passes through the list
# - Inner loop: compares pairs of neighbors and swaps them if needed
for pass_num in range(len(numbers) - 1):
    print(f"\nPass {pass_num + 1}:")
    
    # Go through the list, up to the last unsorted element
    for i in range(len(numbers) - 1 - pass_num):
        # Compare the current item and the next one
        print(f"Compare {numbers[i]} and {numbers[i + 1]}", end=" ")

        # If they’re out of order, swap them
        if numbers[i] > numbers[i + 1]:
            print("→ swap!")
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        else:
            print("→ no change")

        # Show the list after each comparison
        print("Current list:", numbers)

print("\nFinal sorted list:", numbers)

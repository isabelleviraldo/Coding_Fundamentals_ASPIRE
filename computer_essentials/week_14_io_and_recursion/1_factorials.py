def factorial(n, depth=0):
    indent = "  " * depth  # indentation shows recursion depth
    print(f"{indent}→ factorial({n}) called")

    # Base case
    if n == 1:
        print(f"{indent}Returning 1! = 1 (base case)")
        return 1

    # Recursive case
    smaller = factorial(n - 1, depth + 1)
    result = n * smaller
    print(f"{indent}Returning {n}! = {n} * {n-1}! = {result}")
    return result


# Run it
num = int(input("Enter a number to calculate factorial: "))
print("\nStep-by-step recursion trace:\n")
final = factorial(num)

print(f"Final Answer: {num}! = {final}")

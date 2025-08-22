# we're learning functions today!

# A simple function: no input, just prints
def greet():
    print("Hello there!")

#heres how you use a function
greet()

# A function that TAKES input and RETURNS a result
def double(n):
    return n * 2

#lets see how different inputs change the output
# we are puting it inside a print so we can see what the return was
print(double(5))
print(double(7))

#we can take an input and then use the function on that
x = int(input("Give me a number: "))
print("Double is:", double(x))

# A function with multiple parameters
def hypotenuse(a, b):
    # returns (a^2 + b^2)^(1/2)
    return (a**2 + b**2) ** 0.5

#lets see how different inputs change the output
print(hypotenuse(3,4)) # should be 5
print(hypotenuse(5, 12)) # should be 13

# A function that uses default & keyword arguments
def make_profile(name, grade, school="Academy"):
    return f"{name} (Grade {grade}) @ {school}"

#lets see how different inputs change the output
print(make_profile("alex", 11))
print(make_profile(name="sally", grade=10, school="Helix High School"))

# A function that validates input (light defensive coding)
def safe_divide(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

#lets see how different inputs change the output
print(safe_divide(12, 6)) # should be 2
print(safe_divide(12, 0)) # should be "Cannot divide by zero!"

# A function that answers a yes/no question (bool)
def is_palindrome_iterative(text):
    # ch.lower() makes all a letter, and it is doing it to alll the characters in the text
    clean = "".join(ch.lower() for ch in text if ch.isalnum())
    return clean == clean[::-1]  # same forwards/backwards

#now we can input any word we want, and it will check if it is the same
word = input("Type a word to check palindrome: ")
if is_palindrome_iterative(word):
    print("That's a palindrome!")
else:
    print("Not a palindrome.")

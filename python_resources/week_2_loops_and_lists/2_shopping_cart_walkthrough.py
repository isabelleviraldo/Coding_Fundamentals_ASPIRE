# Shopping Cart Simulator

# start with an empty cart
cart = []

print("Welcome to the ASPIRE Shop!")
print("Type 'done' when you are finished shopping.\n")

# keep looping until the user types "done"
item = ""  # make a variable to hold the item we ask for
while item != "done":
    item = input("Add an item to your cart: ")
    if item != "done":     # only add it if it's not "done"
        cart.append(item)
        print(f"{item} has been added to your cart.\n")

# now use a for loop to print everything in the cart
print("\nHere are the items in your cart:")
for thing in cart:
    print("-", thing)

# a fun extra: show how many items are in the cart
print(f"\nYou bought {len(cart)} items today!")

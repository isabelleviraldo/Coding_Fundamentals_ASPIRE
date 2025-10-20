# Pizza Ordering Service

# Ask for the user's name
name = input("Welcome to Python Pizza! What's your name? ")

# Greet the user
print(f"Hi {name}, let's get your order started!")
  
# Ask for pizza size
print("What size pizza would you like?")
print("1. Small\n2. Medium\n3. Large")
size_choice = input("Enter the number of your choice: ")

# Use a match statement to select pizza size and price
match size_choice:
    case "1":
        size = "Small"
        price = 8
    case "2":
        size = "Medium"
        price = 10
    case "3":
        size = "Large"
        price = 12
    case _:
        size = "Medium"
        price = 10
        print("Invalid choice. Defaulting to Medium.")

# Ask for toppings
print("What topping would you like?")
print("1. Pepperoni\n2. Mushrooms\n3. Olives")
topping_choice = input("Enter the number of your topping: ")

# Use a match statement to select topping
match topping_choice:
    case "1":
        topping = "Pepperoni"
    case "2":
        topping = "Mushrooms"
    case "3":
        topping = "Olives"
    case _:
        topping = "Cheese"
        print("Invalid choice. Defaulting to Cheese only.")

# Ask for delivery or pickup
delivery = "no"
delivery = input("Would you like delivery? (yes/no): ")
if delivery == "yes":
    address = input("What's your delivery address? ")
    delivery_fee = 3
else:
    address = "N/A (Pickup)"
    delivery_fee = 0

# Calculate total
total = price + delivery_fee

# Print order summary
print("\n--- Order Summary ---")
print(f"Name: {name}")
print(f"Pizza Size: {size}")
print(f"Topping: {topping}")
print(f"Delivery: {delivery}")
print(f"Address: {address}")
print(f"Total Price: ${total}")
print("Thank you for ordering from Python Pizza!")
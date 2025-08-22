# Library Book Manager
# ----------------------------------------

print("Welcome to the Library Book Manager!")

# This is our starting list of books in the library.
# Lists use square brackets [] and each item is separated by commas.
library = ["The Martian", "Percy Jackson", "Hunger Games", "The Hobbit", "Lord of the Rings"]

# This list will start empty, because the user hasn’t checked out any books yet.
checked_out = []

# This is our first input from the user.
# We ask them what they want to do: checkout, return, or done.
# We save the answer in the variable called "action".
action = input("\nType 'checkout' to borrow a book, 'return' to bring one back, or 'done' to finish: ")

# WHILE LOOP:
# The while loop will keep going until the user types "done".
while action != "done":

    # If the user typed "checkout", we want them to checkout a book.
    if action == "checkout":
        # First, show them what books are available in the library.
        print("\nAvailable books:")

        # FOR LOOP:
        # We use a for loop to print every book in the library with its number.
        # range(len(library)) means "loop from 0 to the number of books - 1".
        for i in range(len(library)):
            # We use i+1 so the numbers start at 1 (easier for humans to read).
            print(f"{i+1}) {library[i]}")

        # Ask which book they want to checkout (by typing the number).
        choice = int(input("Enter the number of the book to checkout: ")) - 1

        # If the choice is valid (in range of the list)...
        if 0 <= choice < len(library):
            # Remove that book from the library list.
            # pop(index) removes the item at that position and also gives it back.
            book = library.pop(choice)

            # Add that book to the checked_out list.
            checked_out.append(book)

            # Tell the user what they just checked out.
            print(f"You checked out '{book}'")
        else:
            print("That number was not valid.")

    # If the user typed "return", we want them to return a book.
    elif action == "return":
        # If they have no books checked out, just say so.
        if len(checked_out) == 0:
            print("You have no books to return.")
        else:
            # Show the list of books they have checked out.
            print("\nBooks you have checked out:")

            # FOR LOOP to list every checked-out book with a number.
            for i in range(len(checked_out)):
                print(f"{i+1}) {checked_out[i]}")

            # Ask which book to return (by typing the number).
            choice = int(input("Enter the number of the book to return: ")) - 1

            # If the choice is valid...
            if 0 <= choice < len(checked_out):
                # Remove it from checked_out list.
                book = checked_out.pop(choice)

                # Add it back to the library list.
                library.append(book)

                # Tell the user what they just returned.
                print(f"You returned '{book}'")
            else:
                print("That number was not valid.")

    # At the end of the loop, ask again what the user wants to do.
    # If they type "done", the loop will end next time.
    action = input("\nType 'checkout' to borrow a book, 'return' to bring one back, or 'done' to finish: ")

# Once the while loop ends, that means the user typed "done".
# Now we show the final state of the library and checked_out lists.

print("\n--- Final Summary ---")

# FOR LOOP to print out the books still in the library.
print("Books still in the library:")
for book in library:
    print("-", book)

# FOR LOOP to print out the books that were checked out.
print("\nBooks you have checked out:")
for book in checked_out:
    print("-", book)

print("\nThanks for visiting the library! Goodbye.")

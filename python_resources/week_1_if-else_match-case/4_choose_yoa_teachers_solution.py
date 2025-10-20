# init variables
has_shears = False


#start program
print("Welcome to the Maze Adventure!")

# Get user name
name = input("What is your name, adventurer? ")
print(f"Good luck, {name}. You're standing at the entrance of a giant maze.")


# First choice
path1 = input("You see two paths: left or right? (left/right): ")
if path1 == "left":
  #now the user can use these shears later if they find the right path
    print("You head left and find a rusty pair of shears. Could be useful.")
    has_shears = True
else:
    print("You head right and pass a mossy statue that seems to be watching you.")

# Second choice
path2 = input("You reach another fork: forward or left? (forward/left): ")
if path2 == "forward":
    print("You walk into a section of the maze full of chirping birds.")
else:
    print("You find a stone archway covered in vines.")

# Third choice - now clearly labeled
print("You arrive at another split in the maze.")
path3 = input("Do you want to go left, right, or forward? (left/right/forward): ")
match path3:
    case "left":
        print("You discover a quiet courtyard with a single tree in the center.")
    case "right":
        if has_shears:
            #they can use their shears now
            use_shears = input("You find a thick hedge. Do you want to use your shears to cut through it? (yes/no): ")
            if use_shears.lower() == "yes":
                print("You cut through the hedge and discover a secret exit!")
            else:
                print("You decide not to use the shears and turn around.")
        else:
            print("A thick hedge blocks the path. You can't go further.")
    case "forward":
        print("You come across a water fountain shaped like a lion's head.")
    case _:
        print("You trip over a root and wander aimlessly for a bit.")

# Fourth choice
path4 = input("Another junction appears: left or right? (left/right): ")
if path4 == "left":
    print("You stumble upon a broken sign that reads 'Do Not Enter'. You go anyway.")
else:
    print("You see the top of a tower through the maze walls — you're getting close.")

# Final choice
print("You reach what seems like the end of your path.")
path5 = input("Do you want to enter the tower, inspect the pond, or climb a tree? (tower/pond/tree): ")
match path5:
    case "tower":
        print("You enter the tower and find a bell. When you ring it, a door opens to the outside!")
    case "pond":
        print("You find something shiny in the water... but it's just an old coin.")
    case "tree":
        print("You climb the tree and see the layout of the maze. You find your way out easily!")
    case _:
        print("You sit down to think — and fall asleep in the grass.")

print("Thanks for playing! Your adventure in the maze comes to an end.")

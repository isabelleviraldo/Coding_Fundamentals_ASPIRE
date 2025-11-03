# Simple Tree Data Structure Demo
# -------------------------------
# This program shows how to represent a tree using a Node class.
# Each Node has a name and a list of children.
# We'll use it to build a small "Animal Tree" and print it neatly.

# Define the Node class
class Node:
    def __init__(self, name):
        self.name = name        # the label for this node (like "Mammals")
        self.children = []      # list to hold this node's child nodes

    def add_child(self, child_node):
        """Add another Node as a child of this one."""
        self.children.append(child_node)

# Recursive function to print the tree nicely
def print_tree(node, level=0):
    indent = "    " * level       # add indentation based on depth
    print(indent + "- " + node.name)
    for child in node.children:   # go through each child node
        print_tree(child, level + 1)

# -------------------------------
# Build our example tree

root = Node("All Animals")

# Level 1 branches
mammals = Node("Mammals")
birds = Node("Birds")
fish = Node("Fish")

root.add_child(mammals)
root.add_child(birds)
root.add_child(fish)

# Level 2 branches
mammals.add_child(Node("Dogs"))
mammals.add_child(Node("Cats"))
mammals.add_child(Node("Whales"))

birds.add_child(Node("Eagles"))
birds.add_child(Node("Penguins"))
birds.add_child(Node("Owls"))

fish.add_child(Node("Sharks"))
fish.add_child(Node("Salmon"))
fish.add_child(Node("Goldfish"))

# -------------------------------
# Print the full tree
print("Animal Classification Tree:\n")
print_tree(root)

class Node:
    def __init__(self, name):
        self.name = name
        self.children = []  # list[Node]

    def add_child(self, child_node):
        self.children.append(child_node)

def build_tree(root):
    """
    Build a tree level-by-level
    For each node in the current layer, we ask for its children (loop until 'q').
    After we finish the entire layer, we optionally continue to the next layer.
    """
    level = [root]        # current layer (list of nodes)
    depth = 0             # depth counter for nice prompts

    while level:
        print(f"\n=== Building Layer {depth} ===")
        next_level = []   # nodes to process in the next layer
        any_new_children = False

        # For each node in THIS layer, gather all its children, then move on
        for node in level:
            print(f"\nAdding children for '{node.name} (q to quit)'")

            while True:
                child_name = input(f"Child of '{node.name}': ").strip()
                if child_name.lower() == 'q':
                    break
                if not child_name:
                    # ignore blank lines; stay on the same node
                    continue

                # create and attach the child
                child = Node(child_name)
                node.add_child(child)
                next_level.append(child)
                any_new_children = True

        # After finishing the whole layer, decide whether to proceed
        if not any_new_children:
            print("\nNo new children added on this layer. Building complete.")
            break

        # Ask if we should continue to build the next layer
        cont = input("\nProceed to build the NEXT layer? (y/n): ").strip().lower()
        if not cont.startswith('y'):
            print("Stopping here. (You can still print the tree.)")
            break

        # Move down to the next layer
        level = next_level
        depth += 1

def print_tree(root):
    """
    Pretty-print the tree with indentation by depth.
    Uses an internal DFS just for printing (doesn't affect BFS building).
    """
    def _print(node, level=0):
        indent = "    " * level
        print(f"{indent}- {node.name}")
        for child in node.children:
            _print(child, level + 1)
    _print(root)

# -------------------------------

root_name = input("Enter the name of the root node (top of the tree): ").strip() or "Root"
root = Node(root_name)

build_tree(root)

print("\nYour completed tree:\n")
print_tree(root)

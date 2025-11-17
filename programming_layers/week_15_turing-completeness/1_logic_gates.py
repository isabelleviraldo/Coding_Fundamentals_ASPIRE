# --------------------------------------------
# Interactive Logic Playground
# --------------------------------------------
# Explore how AND, OR, and NOT combine to form all logic gates.

def AND(a, b):
    return a and b

def OR(a, b):
    return a or b

def NOT(a):
    return not a

# Derived gates (built only from AND, OR, NOT)
def NAND(a, b):
    return NOT(AND(a, b))

def NOR(a, b):
    return NOT(OR(a, b))

def XOR(a, b):
    # true if one is true, not both
    return AND(OR(a, b), NOT(AND(a, b)))

def XNOR(a, b):
    return NOT(XOR(a, b))

# Gate dictionary for easy lookup
GATES = {
    "AND": AND,
    "OR": OR,
    "NOT": NOT,
    "NAND": NAND,
    "NOR": NOR,
    "XOR": XOR,
    "XNOR": XNOR,
}

def show_truth_table(gate_name):
    gate = GATES[gate_name]
    print(f"\n--- Truth Table for {gate_name} ---")
    if gate_name == "NOT":
        print("A | OUT")
        print("--|----")
        for A in [False, True]:
            print(f"{int(A)} | {int(gate(A))}")
    else:
        print("A B | OUT")
        print("----|----")
        for A in [False, True]:
            for B in [False, True]:
                print(f"{int(A)} {int(B)} | {int(gate(A, B))}")
    print("-----------------------------")

def main():
    print("🧠 Welcome to the Logic Gate Playground!")
    print("You can explore these gates: " + ", ".join(GATES.keys()))
    print("Type 'exit' to quit.\n")

    while True:
        gate_name = input("Enter gate name (AND/OR/NOT/NAND/NOR/XOR/XNOR): ").strip().upper()
        if gate_name == "EXIT":
            print("Goodbye!")
            break
        if gate_name not in GATES:
            print("Invalid gate name. Try again.")
            continue

        show_truth_table(gate_name)

        # Optional: Let user test custom inputs
        if gate_name == "NOT":
            a = input("Enter A (0 or 1): ").strip()
            a = a == "1"
            print(f"Result: {int(GATES[gate_name](a))}\n")
        else:
            a = input("Enter A (0 or 1): ").strip()
            b = input("Enter B (0 or 1): ").strip()
            a, b = a == "1", b == "1"
            result = GATES[gate_name](a, b)
            print(f"Result: {int(result)}\n")

if __name__ == "__main__":
    main()

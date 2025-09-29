import random


# ----------------------------
#   DATA / CONSTANTS
# ----------------------------

SIZES = ["Small", "Medium", "Large"]

TOPPINGS = [
    "Pepperoni",
    "Mushroom",
    "Onion",
    "Olive",
    "Bacon",
    "Pineapple",
]


# ----------------------------
#   DISPLAY HELPERS
# ----------------------------

def describe(order):
    """
    Short ticket string for an order (one topping).
    """
    size = order["size"]
    topping = order["topping"]
    return f"{size} | Topping: {topping}"


# === STUDENT TODO (Task 1):
# Add options/weights (e.g., introduce CRUST), or make some toppings appear more often.

def generate_order():
    """
    Make a random order: 1 size + exactly one topping.
    """
    size = random.choice(SIZES)
    topping = random.choice(TOPPINGS)
    return {"size": size, "topping": topping}


# ----------------------------
#   INPUT HELPERS
# ----------------------------

def ask(prompt):
    """
    Input helper that returns None if the user types 'quit' (or 'q').
    """
    s = input(prompt).strip()
    if s.lower() in {"q", "quit"}:
        return None
    return s


def choose_from_list(prompt, options):
    """
    Pick ONE option by number; returns None if user quits.
    """
    print(prompt)
    for i, option in enumerate(options, start=1):
        print(f"  {i}) {option}")

    while True:
        s = ask("> ")
        if s is None:
            return None

        if s.isdigit() and 1 <= int(s) <= len(options):
            index = int(s) - 1
            return options[index]

        print("Pick a number from the list.")


# === STUDENT TODO (Task 2):
# Also allow typing the topping NAME (case-insensitive), not just picking by number.

def choose_one_topping():
    """
    Pick exactly one topping by number; returns None if quit.
    """
    return choose_from_list("Choose TOPPING:", TOPPINGS)


# ----------------------------
#   SCORING
# ----------------------------

def exact_match(order, made):
    """
    True only if size matches AND topping matches.
    """
    return (order["size"] == made["size"]) and (order["topping"] == made["topping"])


# === STUDENT TODO (Task 3):
# Try a partial-credit variant (e.g., +20 if size matches, +5 if topping matches).

def score_pizza(order, made):
    """
    Binary score: +25 for perfect match, else 0.
    """
    return 25 if exact_match(order, made) else 0


# ----------------------------
#   GAME FLOW
# ----------------------------

def make_pizza(n):
    """
    Interactive build for one pizza; returns dict or None if user quits.
    """
    print(f"\n=== Make Pizza #{n} ===")

    size = choose_from_list("Choose SIZE:", SIZES)
    if size is None:
        return None

    topping = choose_one_topping()
    if topping is None:
        return None

    return {"size": size, "topping": topping}


# === STUDENT TODO (Task 4):
# Add a difficulty choice that tweaks generate_order() (e.g., fewer/more sizes, weighted picks).

def play_day():
    """
    Run exactly 4 orders (unless the player quits early).
    """
    print("Welcome to Papa's Pizzeria! (Type 'quit' anytime)")

    total = 0

    for i in range(1, 5):  # exactly 4 orders
        order = generate_order()

        print(f"\n=== ORDER #{i} ===")
        print("Ticket:", describe(order))

        made = make_pizza(i)
        if made is None:
            print("\nGame ended early.")
            break

        gained = score_pizza(order, made)
        total += gained

        result_text = "Correct!" if gained else "Incorrect."
        print(f"Result: {result_text}  +{gained}  Total {total}/100")

    print(f"\nDay complete. Final score: {total}/100")


# ----------------------------
#   ENTRY POINT
# ----------------------------

if __name__ == "__main__":
    random.seed()
    play_day()

>>>>>>> f154ea37221f0a8609f89a0ee82f1e53c3a0ea94
import random

# ----------------------------
#   CONSTANTS / SETTINGS
# ----------------------------
FEED_COST    = 3
CHICKEN_COST = 10
EGG_PRICE    = 5
DEATH_P      = 0.25  # group death chance if any went unfed

# ----------------------------
#   DISPLAY / HELPERS
# ----------------------------
def stats(farm):
    print(
        f"\nDay {farm['day']} | "
        f"Chickens: {farm['chickens']} | "
        f"Coins: {farm['coins']} | "
        f"Feed: {farm['feed']} | "
        f"Fed today: {farm['fed']} | "
        f"Eggs: {farm['eggs']}"
    )

def show_menu():
    print("\nChoose an action:")
    print("  1) Stats")
    print("  2) Buy feed")
    print("  3) Buy chicken")
    print("  4) Feed (all)")
    print("  5) Sell all eggs")
    print("  6) End day (resolve & exit)")
    print("  7) Quit")
    return int(input("> ").strip())

# ----------------------------
#   CORE ACTIONS
# ----------------------------
def buy_feed(farm, n):
    cost = n * FEED_COST
    farm['coins'] -= cost
    farm['feed']  += n
    print(f"Bought {n} feed for {cost} coins.")

def buy_chicken(farm, n):
    cost = n * CHICKEN_COST
    farm['coins']    -= cost
    farm['chickens'] += n
    print(f"Bought {n} chicken(s) for {cost} coins.")

def feed_all(farm):
    need = max(0, farm['chickens'] - farm['fed'])
    
    if farm['chickens'] == 0:
        print("No chickens to feed."); return
    
    if need == 0:
        print("All chickens are already fed today.")
        return
    
    if farm['feed'] >= need:
        farm['feed'] -= need
        farm['fed']  += need
        print(f"Fed all {farm['chickens']} chickens.")
    else:
        missing = need - farm['feed']
        cost    = missing * FEED_COST
        print(f"Not enough feed. Need {missing} more (cost {cost} coins).")
        print(f"Buy with option 2. You have {farm['coins']} coins.")

def sell_all_eggs(farm):
    n = farm['eggs']
    coins = n * EGG_PRICE
    farm['coins'] += coins
    farm['eggs']   = 0
    print(f"Sold {n} egg(s) for {coins} coins.")

def end_day(farm):
    eggs_laid = farm['chickens']            # 1 egg per chicken
    farm['eggs'] += eggs_laid               # keep in storage (not auto-sold)

    unfed = max(0, farm['chickens'] - farm['fed'])
    died  = 1 if (unfed > 0 and random.random() < DEATH_P) else 0
    farm['chickens'] = max(0, farm['chickens'] - died)

    print("\n--- End of Day ---")
    print(f"Fed: {farm['fed']} | Unfed: {unfed} | Deaths: {died}")
    print(f"Eggs laid today: {eggs_laid} | Eggs stored: {farm['eggs']}")

    farm['day'] += 1
    farm['fed']  = 0
    stats(farm)
    print("\nGoodbye!")  # exits after resolving

# ----------------------------
#   MAIN LOOP (match/case)
# ----------------------------
def main():
    farm = {
        "day":       1,
        "coins":     20,
        "chickens":  1,
        "feed":      0,
        
        "fed":       0,
        "eggs":      0,
    }

    print("Welcome to Chicken Farm!")
    stats(farm)

    while True:
        choice = show_menu()

        match choice:
            case 1:  # Stats
                stats(farm)

            case 2:  # Buy feed -> prompt N (with reminder)
                print(f"Feed costs {FEED_COST} each. You have {farm['coins']} coins.")
                n = int(input("How many feed to buy? ").strip())
                buy_feed(farm, n)

            case 3:  # Buy chicken -> prompt N (with reminder)
                print(f"Chickens cost {CHICKEN_COST} each. You have {farm['coins']} coins.")
                n = int(input("How many chickens to buy? ").strip())
                buy_chicken(farm, n)

            case 4:  # Feed (all)
                feed_all(farm)

            case 5:  # Sell all eggs
                sell_all_eggs(farm)

            case 6:  # End day (resolve & exit)
                end_day(farm)
                break

            case 7:  # Quit immediately
                print("Goodbye!")
                break

            case _:
                # With "always correct input" this won't be hit, but kept for completeness.
                print("Enter a number 1-7.")

if __name__ == "__main__":
    random.seed()
    main()

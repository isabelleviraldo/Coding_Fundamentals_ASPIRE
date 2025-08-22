# Example Solution: Mini RPG Adventure
# -------------------------------------------
# This is a simple turn-based RPG battle.
# The player fights against a single monster (a Goblin).
# The player can choose to ATTACK or HEAL each turn.
# The monster will always attack after the player's turn (if it's still alive).
# The battle ends when either the player or the monster runs out of HP.

import random   # we need this for dice rolls (random numbers)

# functions
def roll_dice(sides=6):
    """Return a random number between 1 and 'sides' (inclusive)."""
    return random.randint(1, sides)

def attack(attacker, defender):
    """
    Attacker deals random damage to defender.
    Damage is decided by rolling a 6-sided dice (1 to 6).
    Subtract the damage from the defender's HP.
    """
    dmg = roll_dice(6)  # roll a dice for damage
    defender["hp"] -= dmg  # subtract from defender's HP
    print(f"{attacker['name']} hits {defender['name']} for {dmg} damage!")

def heal(player):
    """
    The player heals a small amount of HP.
    Healing is decided by rolling a 4-sided dice (1 to 4).
    Player's HP cannot go above their max HP.
    """
    amt = roll_dice(4)  # roll a dice for healing
    # new HP is old HP + heal amount, but cannot exceed max HP
    player["hp"] = min(player["hp"] + amt, player["max_hp"])
    print(f"{player['name']} heals for {amt} HP!")

def is_alive(character):
    """
    Check if a character (player or monster) is still alive.
    Returns True if their HP is greater than 0, False otherwise.
    """
    return character["hp"] > 0

# main program
def main():
    # introduction
    print("Welcome to MINI RPG!")
    name = input("Hero, what is your name? ")

    # create player character
    # we use a dictionary to store character information (name, hp, max_hp)
    player = {"name": name or "Hero", "hp": 15, "max_hp": 15}

    # create monster
    monster = {"name": "Goblin", "hp": 12, "max_hp": 12}

    # start of battle
    print(f"A wild {monster['name']} appears!")

    # battle loop (runs while both are alive)
    while is_alive(player) and is_alive(monster):
        # show current HP values
        print(f"\n{player['name']} HP: {player['hp']} | {monster['name']} HP: {monster['hp']}")

        # ask player for action
        choice = input("Choose action: (a)ttack or (h)eal: ").strip().lower()

        # player chooses ATTACK
        if choice == "a":
            attack(player, monster)

        # player chooses HEAL
        elif choice == "h":
            heal(player)

        # invalid input
        else:
            print("Invalid action!")

        # monster takes its turn (only if still alive)
        if is_alive(monster):
            attack(monster, player)

    # battle ends when either the player or monster is not alive
    if is_alive(player):
        print(f"\nYou defeated the {monster['name']}! Victory!")
    else:
        print(f"\nYou were defeated by the {monster['name']}... Game over.")

# standard entry point
# This ensures main() only runs if THIS file is run directly.
if __name__ == "__main__":
    main()

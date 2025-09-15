# Base Character class
class Character:
    def __init__(self, name, hp, attack, weapon):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.weapon = weapon

    def stats(self):
        print(f"\n--- Character Sheet ---")
        print(f"Name: {self.name}")
        print(f"Class: {self.__class__.__name__}")
        print(f"HP: {self.hp}")
        print(f"Attack: {self.attack}")
        print(f"Weapon: {self.weapon}")


# Warrior class
class Warrior(Character):
    def __init__(self, name, weapon):
        super().__init__(name, hp=30, attack=8, weapon=weapon)

    def special(self):
        print(f"{self.name} swings their {self.weapon} mightily!")


# Mage class
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, hp=20, attack=12, weapon="Staff")

    def special(self):
        print(f"{self.name} channels magic through their {self.weapon} and casts Fireball!")


# Rogue class
class Rogue(Character):
    def __init__(self, name):
        super().__init__(name, hp=25, attack=10, weapon="Daggers")

    def special(self):
        print(f"{self.name} sneaks behind the enemy and strikes swiftly with {self.weapon}!")


def rpg_creator():
    print("Welcome to the RPG Character Creator!")

    # get name
    name = input("Enter your character's name: ").strip()

    # choose class
    while True:
        choice = input("Choose a class (warrior/mage/rogue): ").strip().lower()
        if choice == "warrior":
            # let warrior choose weapon
            while True:
                weapon = input("Choose your weapon (sword/axe): ").strip().lower()
                if weapon in ["sword", "axe"]:
                    char = Warrior(name, weapon.capitalize())
                    break
                else:
                    print("Not a valid weapon. Try again.")
            break
        elif choice == "mage":
            char = Mage(name)
            break
        elif choice == "rogue":
            char = Rogue(name)
            break
        else:
            print("Not a valid choice. Try again.")

    print(f"\nYou created {char.name} the {char.__class__.__name__}!")
    char.stats()
    char.special()


if __name__ == "__main__":
    rpg_creator()

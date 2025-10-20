import random
import time

class VirtualCat:
    def __init__(self, name):
        self.name = name
        self.hunger = 5     # 0 = full, 10 = starving
        self.energy = 5     # 0 = exhausted, 10 = full of energy
        self.happiness = 5  # 0 = sad, 10 = very happy
        self.alive = True

    #Keep all stats between 0 and 10, and check if cat is alive.
    def _clamp(self):
        self.hunger = max(0, min(10, self.hunger))
        self.energy = max(0, min(10, self.energy))
        self.happiness = max(0, min(10, self.happiness))

        if self.hunger >= 10 or self.energy <= 0 or self.happiness <= 0:
            self.alive = False

    def feed(self):
        self.hunger -= 3
        self.happiness += 1
        self._clamp()

    def play(self):
        self.happiness += 2
        self.energy -= 1
        self.hunger += 1
        self._clamp()

    def nap(self):
        self.energy += 3
        self.hunger += 1
        self._clamp()

    def status(self):
        return (f"\n{self.name}'s Stats:\n"
                f"  Hunger:    {self.hunger}/10\n"
                f"  Energy:    {self.energy}/10\n"
                f"  Happiness: {self.happiness}/10\n")

    def __del__(self):
        print(f"🐾 Goodbye, {self.name}. The cat has been removed.")


def main():
    print("Virtual Cat Game")
    name = input("What’s your cat’s name? ") or "Whiskers"

    #create virtual cat
    cat = VirtualCat(name)

    #game loop until cat dies
    while cat.alive:
        print(cat.status())
        action = input("Choose [feed/play/nap/quit]: ")

        if action == "feed":
            cat.feed()
            print(f"You fed {cat.name}.")
        elif action == "play":
            cat.play()
            print(f"You played with {cat.name}!")
        elif action == "nap":
            cat.nap()
            print(f"{cat.name} took a nap.")
        elif action == "quit":
            break
        else:
            print("Invalid choice.")

        # small random event
        if random.random() < 0.2:
            print("A toy mouse appears! Happiness +1.")
            cat.happiness += 1
            cat._clamp()

        time.sleep(0.3)

    if not cat.alive:
        print(f"\n Oh no! {cat.name} didn’t make it. Take better care next time!")

    del cat


if __name__ == "__main__":
    main()

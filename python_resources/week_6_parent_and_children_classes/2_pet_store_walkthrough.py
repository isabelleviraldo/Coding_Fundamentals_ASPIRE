# Base Pet class
class Pet:
    def __init__(self, name):
        self.name = name

    def pet(self):
        print(f"You pet {self.name}.")

    def feed(self):
        print(f"You feed {self.name}.")

    def play(self):
        print(f"You play with {self.name}.")


# Dog class
class Dog(Pet):
    def speak(self):
        print(f"{self.name} barks: Woof!")

    def play(self):  # override play
        print(f"You throw a ball. {self.name} fetches it!")


# Cat class
class Cat(Pet):
    def speak(self):
        print(f"{self.name} meows: Meow!")

    def pet(self):  # override play
        print(f"You scratch behind the ears. {self.name} purrs happily.")


def check_out_pet(pet):
    pet.speak()
    while True:
        action = input("Choose an action: pet, feed, play, or back: ")
        if action == "pet":
            pet.pet()
        elif action == "feed":
            pet.feed()
        elif action == "play":
            pet.play()
        elif action == "back":
            break
        else:
            print("Not a valid action.")


# Pet Shop simulation
def pet_shop():
    dog = Dog("Buddy")
    cat = Cat("Luna")

    print("Welcome to the Pet Shop!")
    while True:
        choice = input("\nWhad do you want to check out? [dog/cat/adopt/exit]")
        if choice == "dog":
            print("\nYou walk over to see the dog.")
            check_out_pet(dog)
        elif choice == "cat":
            print("\nYou walk over to see the cat.")
            check_out_pet(cat)
        elif choice == "adopt":
            pick = input("Adopt [dog/cat/exit] ")
            if pick == "dog":
                print(f"You adopted {dog.name} the Dog!")
                break
            elif pick == "cat":
                print(f"You adopted {cat.name} the Cat!")
                break
            else:
                print("You decided not to adopt right now.")
        elif choice == "exit":
            print("You left the Pet Shop. Goodbye!")
            break
        else:
            print("Not a valid choice.")

if __name__ == "__main__":
    pet_shop()

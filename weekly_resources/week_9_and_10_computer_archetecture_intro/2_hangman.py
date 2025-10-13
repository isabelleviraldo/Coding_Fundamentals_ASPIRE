import random

WORDS = [
    "python", "variable", "function", "integer", "boolean",
    "loop", "condition", "string", "debug", "compiler",
]

HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |
     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ==="""
]

def choose_word():
    return random.choice(WORDS)

def show_word(secret, guessed):
    return " ".join([c if c in guessed else "_" for c in secret])

def play_hangman():
    secret = choose_word()
    guessed = set()
    lives = len(HANGMAN_PICS) - 1

    print("=== HANGMAN ===")
    print("Guess the secret word!")

    while lives > 0:
        print(HANGMAN_PICS[len(HANGMAN_PICS) - 1 - lives])
        print("Word:", show_word(secret, guessed))
        print("Guessed:", " ".join(sorted(guessed)))
        print(f"Lives left: {lives}")

        guess = input("Guess a letter: ").lower().strip()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter.\n")
            continue
        if guess in guessed:
            print("You already guessed that!\n")
            continue

        guessed.add(guess)
        if guess not in secret:
            lives -= 1
            print("Wrong!\n")
        else:
            print("Nice guess!\n")

        if all(c in guessed for c in secret):
            print(f"You win! The word was '{secret}'.\n")
            return

    print(HANGMAN_PICS[-1])
    print(f"You lost! The word was '{secret}'.\n")

def main():
    while True:
        play_hangman()
        again = input("Play again? (y/n): ").lower().strip()
        if again != "y":
            print("Bye!")
            break

if __name__ == "__main__":
    main()

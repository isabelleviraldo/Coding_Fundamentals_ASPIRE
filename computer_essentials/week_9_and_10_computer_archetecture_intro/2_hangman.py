import random  # used for choosing a random word

# ---------------- WORD LIST & DRAWINGS ----------------

WORDS = [
    "python", "variable", "function", "integer", "boolean",
    "loop", "condition", "string", "debug", "compiler",
]

# Stages of the hangman drawing — from no mistakes to game over
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

# ---------------- HELPER FUNCTIONS ----------------

def choose_word():
    """Pick a random secret word from the list."""
    return random.choice(WORDS)


def letter_in_word(letter, word):
    """Return True if the letter is in the word, False otherwise."""
    if letter in word:
        print(f"Yes! '{letter}' is in the word.")
        return True
    else:
        print(f"Nope! '{letter}' isn’t in the word.")
        return False


def update_display_word(secret, guessed):
    """
    Create a display version of the secret word with guessed letters shown
    and the rest as underscores.
    Example: secret='loop', guessed={'o'} -> '_ o o _'
    """
    display = ""
    for c in secret:
        if c in guessed:
            display += c + " "
        else:
            display += "_ "
    return display.strip()


def print_hangman(lives_remaining, total_lives):
    """
    Prints the correct hangman drawing based on how many lives are left.
    Example: if total=6 and remaining=3, print the halfway-done drawing.
    """
    stage_index = total_lives - lives_remaining
    stage_index = min(stage_index, len(HANGMAN_PICS) - 1)  # safety clamp
    print(HANGMAN_PICS[stage_index])


# ---------------- MAIN GAME FUNCTION ----------------

def play_hangman():
    """Run one full round of Hangman."""
    secret = choose_word()                # the word to guess
    guessed = set()                       # store guessed letters
    total_lives = len(HANGMAN_PICS) - 1   # total number of lives
    lives = total_lives                   # current lives

    print("=== HANGMAN ===")
    print("Guess the secret word!")

    while lives > 0:
        # show the hangman drawing for current state
        print_hangman(lives, total_lives)

        # show current state of the word
        print("Word:", update_display_word(secret, guessed))
        print("Guessed:", " ".join(sorted(guessed)))
        print(f"Lives left: {lives}")

        # ask the user for their guess
        guess = input("Guess a letter: ").lower().strip()

        # validate the guess
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter.\n")
            continue
        if guess in guessed:
            print("You already guessed that!\n")
            continue

        # add to guessed letters
        guessed.add(guess)

        # check the guess using our helper
        if not letter_in_word(guess, secret):
            lives -= 1  # lose a life for a wrong guess
        print()

        # check win condition: all letters guessed
        if all(c in guessed for c in secret):
            print(f" You win! The word was '{secret}'.\n")
            return

    # if loop ends, player ran out of lives
    print_hangman(0, total_lives)
    print(f" You lost! The word was '{secret}'.\n")


# ---------------- MAIN LOOP ----------------

def main():
    """Allows players to replay multiple times."""
    while True:
        play_hangman()
        again = input("Play again? (y/n): ").lower().strip()
        if again != "y":
            print("Bye!")
            break


# Run game when file is executed
if __name__ == "__main__":
    main()

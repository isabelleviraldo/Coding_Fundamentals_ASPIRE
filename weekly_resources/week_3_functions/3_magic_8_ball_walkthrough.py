# Magic 8-Ball — functions

import random

#all possible answers
answers = [
    "It is certain.", "Without a doubt.", "You may rely on it.", "Yes — definitely.",
    "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
    "Reply hazy, try again.", "Ask again later.", "Better not tell you now.",
    "Cannot predict now.", "Concentrate and ask again.",
    "Don't count on it.", "My reply is no.", "Outlook not so good.",
    "Very doubtful.", "Absolutely not."
]

#pure functions
def random_answer():
    """Pick and return one answer string."""
    return random.choice(answers)

def keep_going(resp: str):
    """Return True if the user wants to ask another question."""
    return resp.strip().lower() in {"y", "yes", "ok", "again", "more"}

# functions that print stuff
def get_question():
    """Ask the user for a yes/no style question and return it."""
    return input("\nAsk the Magic 8-Ball a yes/no question: ")

def show_answer(ans: str):
    """Print the 8-ball's answer."""
    print(f" 🎱 {ans}")

# main function
def main():
    print("Welcome to the Magic 8-Ball!")
    name = input("What's your name? ")
    print(f"Hi {name or 'Seeker'} — think carefully...")

    while True:
        _ = get_question()   # we don't actually use what they enter
        show_answer(random_answer())
        again = input("Ask another? (y/n): ")
        if not keep_going(again):
            print("Farewell! 🔮")
            break

# standard entry point (only runs when executed directly)
if __name__ == "__main__":
    main()

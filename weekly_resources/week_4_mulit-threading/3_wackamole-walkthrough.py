import threading   # lets us run code in separate "threads" at the same time
import time        # for sleeping (delays) and checking the clock
import random      # for choosing random mole holes

#global variables
GAME_SECONDS = 20          # how long the game runs
MOLE_LIFETIME = 1.5        # how many seconds a mole stays before disappearing

# shared variables
# these variables are seen by both the main thread and the spawner thread
current_mole = None   # the current hole with a mole (None = no mole showing)
score = 0             # player’s score
game_over = False     # flag that ends the spawner thread when time is up

def spawner():
    # This is the background thread function.
    # Its job is to make moles appear in random holes,
    # keep them up for a short time, and then remove them if not hit.


    global current_mole, game_over

    while not game_over:   # keep going until game is over
        # wait a little before spawning the next mole
        # (random gap so it's not predictable)
        time.sleep(random.uniform(0.5, 1.5))

        if game_over:      # check again in case time just ran out
            break

        # choose a random hole for the mole to pop up
        current_mole = random.randint(1, 5)
        print(f"\nMole at hole {current_mole}!")

        # keep it visible for MOLE_LIFETIME seconds
        time.sleep(MOLE_LIFETIME)

        # if the mole is still there after that time, it escaped
        if current_mole is not None:
            print("The mole got away!")
            current_mole = None   # clear it

def main():
    global current_mole, score, game_over

    random.seed()  # make the randomness different each run

    # intro message
    print("=== Whack-a-Mole ===")
    print("Type 1, 2, 3, 4, or 5 to whack that hole!")
    print(f"Game lasts {GAME_SECONDS} seconds.\n")

    # start the mole spawner thread
    # This thread will keep printing mole appearances in the background
    spawner_thread = threading.Thread(target=spawner)
    spawner_thread.start()

    # Main loop 
    start_time = time.time()
    while time.time() - start_time < GAME_SECONDS:   # run until time is up
        hole_num = int(input("whack where? "))

        # check if the guess matches the current mole
        if current_mole == hole_num:
            print("HIT!")
            score += 1          # increase score
            current_mole = None # clear mole so it can’t be hit twice
        else:
            print("MISS!")

    # end the game
    game_over = True              # tell spawner thread to stop
    spawner_thread.join()         # wait for spawner thread to finish

    #game over screen
    print("\n=== Game Over ===")
    print(f"Final score: {score}")
    print("Thanks for playing!")

# Only run the game if this file is executed directly
if __name__ == "__main__":
    main()

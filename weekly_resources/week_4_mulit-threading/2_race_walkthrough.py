#here are some libraries we will be using
import threading
import time
import random

# global variables
LAPS_TO_WIN = 10
#racer names
RACER_1 = "Penny"
RACER_2 = "Zach"
RACER_3 = "Sam"


# Global flag: False until someone wins, then set to True
isRaceOver = False

def runner(name):
    #Loops through 10 laps, sleeping a random FLOAT each lap.
    #The first runner to finish all laps sets raceOver=True and declares victory.

    #set the isRaceOver variable as a global variable
    global isRaceOver

    #run the laps, each lap takes a random amount of time
    for lap in range(1, LAPS_TO_WIN + 1):
        # Random FLOAT delay (e.g., 1.27s), not just 1/2/3
        lap_time = random.uniform(1.0, 3.0)
        time.sleep(lap_time)
        print(f"{name} finished lap {lap} (took {lap_time:.2f}s)")

    # After completing all laps, try to declare victory if race not yet marked over.
    if not isRaceOver:
        isRaceOver = True
        print(f"{name} IS THE WINNER!")

def main():
    random.seed()  # different timing each run
    print("3… 2… 1… GO!")

    # --- Explicitly create each thread (no loops for clarity) ---
    t1 = threading.Thread(target=runner, args=(RACER_1,))
    t2 = threading.Thread(target=runner, args=(RACER_2,))
    t3 = threading.Thread(target=runner, args=(RACER_3,))

    #run each of the threads
    t1.start()
    t2.start()
    t3.start()

    #close the threads once theyre done
    t1.join()
    t2.join()
    t3.join()

    print("Race complete!")

if __name__ == "__main__":
    main()

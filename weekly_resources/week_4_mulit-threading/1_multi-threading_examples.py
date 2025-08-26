#this is a library so we can wait an amount of time
import time

#this library allows us to multi-thread functions
import threading

#this will print A 5 times, then B five times
def beep(letter, delay):
    for i in range(5):
        print(letter)
        time.sleep(delay)

beep("A", 0.5)
beep("B", 0.5)

#instead, lets set up 2 threads, with the same arguments, and run them simultaneously
t1 = threading.Thread(target=beep, args=("A", 0.5))
t2 = threading.Thread(target=beep, args=("B", 0.5))
#start both of the threads
t1.start()
t2.start()
#end both the threads once theyve completed
t1.join()
t2.join()
print("Done!")




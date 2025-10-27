"""
Workshop 1: Cache Intuition & Locality
--------------------------------------
Goal:
  Show that accessing memory in a predictable (sequential) way
  is faster than accessing it randomly, due to CPU cache behavior.

Concepts:
  - Spatial Locality: Nearby memory locations are often accessed together.
  - Temporal Locality: Recently used data is likely to be used again soon.
  - Cache makes sequential access faster since nearby data stays in CPU cache.
"""

import time
import random

# -------------------------------
# STEP 1: Create a large list of numbers to simulate "memory"
# -------------------------------
N = 10_000_000   # 10 million elements
data = [i for i in range(N)]  # pretend this is our "main memory"

# -------------------------------
# STEP 2: Sequential Access
# -------------------------------
# This loop goes through the list one element at a time, in order.
# Because each next element is right next to the previous one in memory,
# the CPU cache can easily "predict" what comes next.
start = time.perf_counter()  # record start time
total = 0
for i in range(N):
    total += data[i]
end = time.perf_counter()    # record end time
print(f"Sequential time: {end - start:.4f} seconds")

# -------------------------------
# STEP 3: Random Access
# -------------------------------
# Now we access the same list in a *random* order.
# This breaks spatial locality — each lookup might be far from the last,
# so the CPU has to reload different chunks of memory into cache.
indices = [random.randint(0, N - 1) for _ in range(N)]
start = time.perf_counter()
total = 0
for i in indices:
    total += data[i]
end = time.perf_counter()
print(f"Random time: {end - start:.4f} seconds")

# -------------------------------
# STEP 4: Discussion
# -------------------------------
# Typically, you'll see that sequential access is faster than random access.
# Why? Because cache stores nearby data.
# When you jump around randomly, the CPU cache can't predict or reuse data.
# This demonstrates the idea of *spatial locality*.

"""
Workshop 2: Simulating Cache Behavior
-------------------------------------
Goal:
  Understand how a CPU cache works internally — specifically,
  what a 'cache hit' and 'cache miss' mean.

Concepts:
  - A cache stores a small set of recently accessed memory addresses.
  - If the requested address is already in the cache → HIT.
  - If it’s not in the cache → MISS, and the data must be fetched (slow).
  - This simple model is a *direct-mapped* cache.
"""

# -------------------------------
# STEP 1: Define the cache simulator function
# -------------------------------
def simulate_cache(memory_accesses, cache_size):
    """
    Simulates a simple *direct-mapped cache*.

    Parameters:
      memory_accesses (list[int]): the memory addresses accessed by the CPU.
      cache_size (int): number of cache slots available.

    Returns:
      (hits, misses) -> how many times data was found or not found in cache.
    """
    cache = [-1] * cache_size  # start with all cache slots empty (-1 = empty)
    hits, misses = 0, 0        # keep count of both events

    # Loop through each address in the access sequence
    for addr in memory_accesses:

        # Each address maps to one *specific* cache slot
        # This is the "direct-mapped" part.
        index = addr % cache_size

        # If the cache slot already has this address, it’s a hit
        if cache[index] == addr:
            hits += 1
            print(f"Access {addr:2d}: HIT  (cache[{index}] = {addr})")

        # Otherwise, it’s a miss — replace that slot with the new address
        else:
            misses += 1
            print(f"Access {addr:2d}: MISS (replacing cache[{index}] with {addr})")
            cache[index] = addr  # simulate bringing it into cache

    # Return total stats
    return hits, misses


# -------------------------------
# STEP 2: Example sequence of memory accesses
# -------------------------------
# This represents the "memory addresses" that a CPU might try to read.
# We use small numbers for clarity.
accesses = [0, 1, 2, 3, 4, 5, 0, 1, 2, 3, 4, 5]

# Try different cache sizes to see how performance changes
cache_size = 4

print(f"\nSimulating with cache size = {cache_size}...\n")

# -------------------------------
# STEP 3: Run the simulation
# -------------------------------
hits, misses = simulate_cache(accesses, cache_size)

# -------------------------------
# STEP 4: Show final results
# -------------------------------
print("\nSimulation complete!")
print(f"Total Hits:   {hits}")
print(f"Total Misses: {misses}")
hit_rate = hits / len(accesses)
print(f"Hit Rate:     {hit_rate:.2%}")

# -------------------------------
# STEP 5: Experiment ideas for students
# -------------------------------
# 1. Change cache_size (try 2, 4, 8) and see how it affects hit rate.
# 2. Change the access pattern (e.g., repeat same few addresses).
# 3. Add print statements to show the cache contents at each step.
# 4. Discuss how a *larger cache* or *better mapping* improves hits.

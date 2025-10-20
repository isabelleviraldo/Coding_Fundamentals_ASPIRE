# Simulate multiple CPU cores (threads) running simple ADD/SUB programs
# Each "core" is a thread, each "program" is a list of fake instructions

import threading, time, random

# --- Define our 4 tiny programs ---
# Each program has a few ADD/SUB instructions that change an accumulator (ACC)
PROGRAMS = {
    1: [("ADD", 5), ("ADD", 3), ("SUB", 2), ("ADD", 4), ("SUB", 1)],
    2: [("ADD", 2), ("SUB", 1), ("ADD", 2), ("ADD", 2), ("SUB", 3), ("ADD", 6)],
    3: [("SUB", 2), ("ADD", 9), ("SUB", 4), ("ADD", 1), ("SUB", 1), ("ADD", 3)],
    4: [("ADD",10), ("SUB", 3), ("SUB", 2), ("ADD", 1), ("ADD", 1)],
}

# Small timing controls so outputs don't overlap perfectly
ALU_STEP = 0.07   # seconds per "instruction"
JITTER   = 0.02   # small randomness for realism

# --- Function each "core" thread will run ---
def core_worker(core_name, prog_ids):
    """Each core runs one or more programs sequentially."""
    if not prog_ids:
        print(f"{core_name} has no programs assigned.")
        return

    for pid in prog_ids:
        acc = 0  # the program's local accumulator (like a CPU register)
        start = time.perf_counter()

        # Run through each instruction
        for op, val in PROGRAMS[pid]:
            # Perform the operation
            acc = acc + val if op == "ADD" else acc - val
            # Sleep a little to simulate instruction time
            time.sleep(ALU_STEP + random.uniform(0, JITTER))

        elapsed = time.perf_counter() - start
        print(f"{core_name} COMPLETED Program {pid} in {elapsed:.3f}s (ACC={acc})")

# --- Decide which cores get which programs ---
def assign_programs(n):
    """
    Returns a mapping like:
      { "Core-1":[1,2], "Core-2":[3,4] }
    based on how many cores are entered.
    """
    if n < 1: n = 1  # always at least 1 core
    names = [f"Core-{i}" for i in range(1, n + 1)]
    mapping = {name: [] for name in names}

    # Rule set per user spec
    if n == 1:
        mapping["Core-1"] = [1, 2, 3, 4]
    elif n == 2:
        mapping["Core-1"], mapping["Core-2"] = [1, 2], [3, 4]
    elif n == 3:
        # one random core gets 2 programs, others get 1
        lucky = random.choice(names[:3])
        base = {"Core-1": [1], "Core-2": [2], "Core-3": [3]}
        for k, v in base.items():
            if k in mapping: mapping[k] = v
        mapping[lucky].append(4)
    else:
        # 4+ cores: first 4 get one each; extras do nothing
        base = {"Core-1": [1], "Core-2": [2], "Core-3": [3], "Core-4": [4]}
        for k, v in base.items():
            if k in mapping: mapping[k] = v

    return mapping

# --- Main program flow ---
def main():
    print("CPU core simulator — each program is a short list of ADD/SUB steps.")
    try:
        n = int(input("Enter number of cores (1, 2, 3, 4, ...): ").strip())
    except Exception:
        n = 1
        print("Invalid input, defaulting to 1 core.")

    # Get the assignment of programs to cores
    mapping = assign_programs(n)

    # Print out what each core will do
    print("\nAssignment:")
    def core_index(name): return int(name.split("-")[1])
    for name in sorted(mapping, key=core_index):
        progs = mapping[name]
        if progs:
            print(f"{name} will run programs {progs}")
        else:
            print(f"{name} will run no programs")

    # Create and start a thread for each core
    threads = []
    for name, progs in mapping.items():
        t = threading.Thread(target=core_worker, args=(name, progs))
        t.start()
        threads.append(t)

    # Wait for all threads to finish
    for t in threads:
        t.join()

    print("\nAll assigned programs complete. Done!")

# --- Run the main function ---
if __name__ == "__main__":
    main()

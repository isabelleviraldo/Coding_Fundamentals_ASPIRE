import time

# --- global delays (seconds) ---
IO_DELAY   = 0.05
RAM_DELAY  = 0.10
CPU_DELAY  = 0.02
DISK_DELAY = 0.40

# --- system state ---
keyboard_buffer = []     # RAM: Keyboard Buffer
document_buffer = []     # RAM: Document Buffer
storage = {}             # Storage: filename -> contents

def wait_time(label, secs, extra=""):
    time.sleep(secs)
    print(f"{label} ~ {secs:.2f}s {extra}")

def show_state(filename):
    kb = "".join(keyboard_buffer)
    doc = "".join(document_buffer)
    size_doc = len(doc)
    size_kb = len(kb)
    size_file = len(storage.get(filename, ""))

    print("\n=== COMPUTER STATE ===")
    print(f"RAM - Keyboard Buffer: {size_kb} chars")
    print(f"  Preview: {kb[:40].replace('\\n','↩')} {'...' if size_kb>40 else ''}")
    print(f"RAM - Document Buffer: {size_doc} chars")
    print(f"  Preview: {doc[:40].replace('\\n','↩')} {'...' if size_doc>40 else ''}")
    print(f"Storage - Files: {list(storage.keys()) or '[]'}")
    if filename in storage:
        print(f"  '{filename}': {size_file} bytes")
    print("======================\n")

# 1) I/O → RAM (Keyboard Buffer)
def io_to_ram(text, filename):
    wait_time("[I/O] Keyboard input received", IO_DELAY, f"{len(text)} chars")
    wait_time("[RAM] Place chars into Keyboard Buffer", RAM_DELAY)
    for ch in text:                 # no .extend; make it explicit for students
        keyboard_buffer.append(ch)
    show_state(filename)

# 2) RAM (Keyboard Buffer) → CPU → RAM (Document Buffer)
def cpu_move_to_document(filename):
    moved = 0
    while len(keyboard_buffer) > 0:
        wait_time("[RAM] CPU reads next char from Keyboard Buffer", RAM_DELAY)
        ch = keyboard_buffer[0]     # no .pop()
        del keyboard_buffer[0]      # remove first char explicitly
        show_state(filename)

        wait_time("[CPU] Decide/append to Document Buffer", CPU_DELAY, f"'{ch}'")
        wait_time("[RAM] Write char to Document Buffer", RAM_DELAY)
        document_buffer.append(ch)
        moved += 1
        show_state(filename)
    print(f"[App] Document Buffer updated (+{moved} chars).")

# 3) RAM (Document Buffer) → Storage (File)
def save_to_storage(filename):
    wait_time("[CPU] Prepare data for saving", CPU_DELAY)
    wait_time("[RAM] Gather bytes from Document Buffer", RAM_DELAY)
    data = "".join(document_buffer)
    wait_time("[Storage] Persist bytes to file", DISK_DELAY, f"{len(data)} bytes")
    storage[filename] = data
    print(f"[Result] Saved '{filename}' ({len(data)} bytes).")
    show_state(filename)

def show_document():
    print("\n--- RAM: Document Buffer ---")
    print("".join(document_buffer), end="")
    print("\n----------------------------")

def main():
    filename = "document.txt"
    print("Commands: /show   /save   /quit")
    print("Anything else = append that line to the document.\n")

    while True:
        line = input("> ")
        if line == "/show":
            show_document()
        elif line == "/save":
            save_to_storage(filename)
        elif line == "/quit":
            save_to_storage(filename)
            break
        else:
            # I/O → RAM
            io_to_ram(line + "\n", filename)
            # CPU ↔ RAM
            cpu_move_to_document(filename)

    print("\n--- STORAGE: final file ---")
    print(storage.get(filename, ""))

if __name__ == "__main__":
    main()

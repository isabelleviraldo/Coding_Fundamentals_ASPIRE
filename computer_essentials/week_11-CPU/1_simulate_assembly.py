# tiny_cpu.py
# Simulate a CPU executing instructions step-by-step.

class CPU:
    def __init__(self):
        self.pc = 0          # program counter
        self.acc = 0         # accumulator register
        self.running = True

def run(program):
    cpu = CPU()
    while cpu.running:
        instr = program[cpu.pc]
        op = instr[0]
        args = instr[1:]
        print(f"[PC={cpu.pc}] ACC={cpu.acc:3d} -> {op} {args}")

        if op == "LOAD":
            cpu.acc = int(args[0])
            cpu.pc += 1
        elif op == "ADD":
            cpu.acc += int(args[0])
            cpu.pc += 1
        elif op == "SUB":
            cpu.acc -= int(args[0])
            cpu.pc += 1
        elif op == "PRINT":
            print(f"OUTPUT: {cpu.acc}")
            cpu.pc += 1
        elif op == "HALT":
            cpu.running = False
        else:
            raise ValueError(f"Unknown opcode {op}")

if __name__ == "__main__":
    # A tiny program that adds and subtracts like a CPU.
    program = [
        ("LOAD", 10),
        ("ADD", 5),
        ("ADD", 3),
        ("SUB", 4),
        ("PRINT",),
        ("HALT",),
    ]
    run(program)

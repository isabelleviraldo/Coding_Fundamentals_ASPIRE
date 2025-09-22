# calc.py
# Day 1: super simple two-number calculator.
# Assumptions: input looks like number<op>number (e.g., 12+34), no spaces, one operator.
# We'll add tiny upgrades on Day 2 where you see "==== DAY 2".

# ---- operator functions (no lambdas) ----
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

# We'll only allow these for Day 1.
ALLOWED_OPS = "+-*/"
# ==== DAY 2: we'll add '^' here to support power.

def find_operator(expr: str):
    """Return (index, op) for the single operator in expr, or raise if not found."""
    for i, ch in enumerate(expr):
        if ch in ALLOWED_OPS:
            return i, ch
    raise ValueError("no operator found (use + - * /)")

def parse_two_numbers(expr: str):
    """Split 'A<op>B' into (A:int, op:str, B:int). Day 1 uses integers."""
    i, op = find_operator(expr)
    left = expr[:i]
    right = expr[i+1:]
    if left == "" or right == "":
        raise ValueError("need number<op>number")
    # Day 1: integers only to keep it simple
    a = int(left)
    b = int(right)
    return a, op, b

def apply(a, op, b):
    """Compute a <op> b using our basic ops."""
    if op == "+": return add(a, b)
    if op == "-": return sub(a, b)
    if op == "*": return mul(a, b)
    if op == "/": return div(a, b)
    # ==== DAY 2: we'll handle '^' here.
    raise ValueError(f"unknown operator: {op}")

class Calculator:
    def evaluate(self, expr: str):
        # Assumes expr like '12+34' (no spaces).
        a, op, b = parse_two_numbers(expr)
        result = apply(a, op, b)
        return result

def repl():
    print("Day 1: two-number calculator. Examples: 12+34, 9*5, 10/2   ('q' to quit)")
    calc = Calculator()
    while True:
        s = input("> ")
        if s.lower() in {"q", "quit", "exit"}:
            break
        try:
            print(calc.evaluate(s))
        except Exception as e:
            print("error:", e)

if __name__ == "__main__":
    # Quick checks:
    # 7+3 -> 10
    # 9-4 -> 5
    # 6*5 -> 30
    # 8/2 -> 4
    repl()

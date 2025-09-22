# calc.py — Day 2
# Upgrades from Day 1:
#  - Allow decimals (parse as float)
#  - Add power operator '^'
# Assumptions: input is exactly number<op>number (e.g., 12.5*3, 2^8), no spaces.

# ---- operator functions (no lambdas) ----
def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b
def power(a, b): return a ** b

# Day 2: added '^'
ALLOWED_OPS = "+-*/^"

def find_operator(expr: str):
    """Return (index, op) for the single operator in expr, or raise if not found."""
    for i, ch in enumerate(expr):
        if ch in ALLOWED_OPS:
            return i, ch
    raise ValueError("no operator found (use + - * / ^)")

def parse_two_numbers(expr: str):
    """
    Split 'A<op>B' into (A:float, op:str, B:float).
    Keeps things simple: one operator, no spaces, non-negative numbers.
    """
    i, op = find_operator(expr)
    left = expr[:i]
    right = expr[i+1:]
    if left == "" or right == "":
        raise ValueError("need number<op>number (e.g., 12.5*3)")
    a = float(left)
    b = float(right)
    return a, op, b

def apply(a, op, b):
    """Compute a <op> b using our basic ops."""
    if op == "+": return add(a, b)
    if op == "-": return sub(a, b)
    if op == "*": return mul(a, b)
    if op == "/": return div(a, b)
    if op == "^": return power(a, b)
    raise ValueError(f"unknown operator: {op}")

class Calculator:
    def evaluate(self, expr: str):
        a, op, b = parse_two_numbers(expr)
        return apply(a, op, b)

def repl():
    print("Day 2: two-number calculator with decimals and '^'. Examples:")
    print("  3.5+2.5   10/4   2^3   7*0.5   ('q' to quit)")
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
    # Quick acceptance checks you can try:
    # 3.5+2.5 -> 6.0
    # 10/4    -> 2.5
    # 2^3     -> 8.0
    # 7*0.5   -> 3.5
    repl()

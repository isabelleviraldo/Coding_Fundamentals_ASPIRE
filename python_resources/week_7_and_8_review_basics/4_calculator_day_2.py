def add(a,b): return a + b
def sub(a,b): return a - b
def mult(a,b): return a * b

def div(a,b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

def mod(a,b):
    if b == 0:
        raise ZeroDivisionError("modulo by zero")
    return a % b

def power(a,b):
    return a ** b

# We keep the original two-number path, now with % and ^
ALLOWED_OPS = "+-*/%^"

def find_operator(expression):
    # Very simple: find the first operator char in the string
    for i, ch in enumerate(expression):
        if ch in ALLOWED_OPS:
            return i, ch
    raise ValueError("no operator found (use + - * / % ^)")

def parse_two_numbers(expression):
    # Trim spaces around the two sides; allow decimals
    i, op = find_operator(expression)

    left = expression[0:i].strip()
    right = expression[i+1:].strip()

    # NOTE: This simple version does NOT support a leading + or - on the left number
    # (e.g., "-3+2"). Keep inputs positive or write them as (0-3)+2 for now.
    a = float(left)
    b = float(right)
    return a, op, b

def apply(a, op, b):
    if op == "+": return add(a,b)
    if op == "-": return sub(a,b)
    if op == "*": return mult(a,b)
    if op == "/": return div(a,b)
    if op == "%": return mod(a,b)
    if op == "^": return power(a,b)
    raise ValueError(f"unknown operator:{op}")

# -------------------------------
# Minimal tokenization (add/sub)
# -------------------------------
# Goal: show how we can scan characters, build number tokens, collect + / -,
# and then evaluate left-to-right for exactly THREE numbers (A op B op C).
#
# Rules for this mini-tokenizer:
#   - Allowed operators here are ONLY '+' and '-'
#   - Numbers can be decimals (e.g., 3.14). No unary +/- (keep it simple).
#   - Spaces are ignored.
#   - Input must contain exactly 3 numbers and 2 operators.
#
# Examples: "1+2+3", "10.5 - 3 + 1.25"
def tokenize_add_sub_3(expr):
    nums = []
    ops = []

    s = expr.replace(" ", "")  # ignore spaces
    i = 0
    n = len(s)

    def read_number(start):
        j = start
        seen_dot = False
        # read digits and at most one '.'
        while j < n and (s[j].isdigit() or (s[j] == '.' and not seen_dot)):
            if s[j] == '.':
                seen_dot = True
            j += 1
        if j == start:
            raise ValueError("expected a number")
        return float(s[start:j]), j

    # read first number
    a, i = read_number(0)
    nums.append(a)

    # read (op, number) twice
    for _ in range(2):
        if i >= n or s[i] not in "+-":
            raise ValueError("expected '+' or '-'")
        ops.append(s[i])
        i += 1

        b, i = read_number(i)
        nums.append(b)

    if i != n:
        raise ValueError("extra characters at end (only A op B op C allowed)")

    return nums, ops

def eval_add_sub_3(expr):
    nums, ops = tokenize_add_sub_3(expr)
    # left-to-right: ((A op B) op C)
    result = nums[0]
    for k, op in enumerate(ops):
        if op == '+':
            result = result + nums[k+1]
        else:
            result = result - nums[k+1]
    return result

# Helper to decide when to use the 3-number tokenizer:
def is_three_term_add_sub(expr):
    # True if contains exactly 2 operators and all are +/-, and contains no * / % ^
    s = expr.replace(" ", "")
    if any(op in s for op in "*/%^"):
        return False
    plus_minus_positions = [i for i,ch in enumerate(s) if ch in "+-"]
    return len(plus_minus_positions) == 2

class Calculator:
    def evaluate(self, expression):
        # If it's a simple 3-term +/-, show tokenization/eval path
        if is_three_term_add_sub(expression):
            return eval_add_sub_3(expression)

        # Otherwise, fall back to the original two-number path with more ops
        a, op, b = parse_two_numbers(expression)
        return apply(a, op, b)

def main():
    print("Welcome to the calculator:")
    print(" - Two-number ops: + - * / % ^ (decimals allowed)")
    print(" - Three-number demo (tokenization): A +/- B +/- C (e.g., '1.5+2-3')")
    print(" - Type 'quit' to exit.\n")

    calc = Calculator()
    while True:
        user_input = input("> ")
        if user_input.strip().lower() == "quit":
            break

        try:
            print(calc.evaluate(user_input))
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

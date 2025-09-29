

def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mult(a,b):
    return a * b
def div(a,b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b
    

ALLOWED_OPS = "+-*/"

def find_operator(expression):
    for i, ch in enumerate(expression):
        if ch in ALLOWED_OPS:
            return i, ch
    raise ValueError("no operator found (use + - * /)")

def parse_two_numbers(expression):
    i, op = find_operator(expression)
    
    left = expression[0:i]
    right = expression[i+1:]
    
    a = int(left)
    b = int(right)
    
    return a, op, b
    
def apply(a, op, b):
    if op == "+":
        return add(a,b)
    if op == "-":
        return sub(a,b)
    if op == "*":
        return mult(a,b)
    if op == "/":
        return div(a,b)
        
    raise ValueError(f"unknown operator:{op}")

class Calculator:
    def evaluate(self, expression):
        a, op, b = parse_two_numbers(expression)
        result = apply(a, op, b)
        return result

def main():
    print("Welcome to the calculator:")
    
    calc = Calculator()
    while(True):
        user_input = input("> ")
        if user_input == "quit":
            break
        
        print(calc.evaluate(user_input))

if __name__ == "__main__":
    main()






    


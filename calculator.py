class Calculator:
    """Simple calculator supporting basic arithmetic operations."""

    def add(self, a: float, b: float) -> float:
        """Return the sum of a and b."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Return the difference of a and b."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Return the product of a and b."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Return the quotient of a and b. Raises ZeroDivisionError if b is zero."""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b


def main():
    calc = Calculator()
    print("Simple Calculator")
    print("Select operation: +, -, *, /")
    op = input("Operation: ")
    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers.")
        return

    try:
        if op == '+':
            result = calc.add(a, b)
        elif op == '-':
            result = calc.subtract(a, b)
        elif op == '*':
            result = calc.multiply(a, b)
        elif op == '/':
            result = calc.divide(a, b)
        else:
            print("Unsupported operation")
            return
    except ZeroDivisionError as exc:
        print(exc)
        return

    print("Result:", result)


if __name__ == "__main__":
    main()

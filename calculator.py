import math
import re

class Calculator:
    def __init__(self):
        # Stores variables and memory operations
        self.memory = 0
        self.variables = {}

    def add(self, a, b):
        """Add two numbers."""
        return a + b

    def subtract(self, a, b):
        """Subtract b from a."""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b

    def divide(self, a, b):
        """Divide a by b, handle divide-by-zero gracefully."""
        if b == 0:
            return "Error: Division by zero"
        return a / b

    def store_in_memory(self, value):
        """Store a number in memory."""
        self.memory = value

    def recall_memory(self):
        """Return the last stored value."""
        return self.memory

    def clear_memory(self):
        """Clear the stored memory value."""
        self.memory = 0

    def assign_variable(self, name, value):
        """Assign a variable (like x = 5)."""
        self.variables[name] = value

    def evaluate_expression(self, expr):
        """
        Evaluate a mathematical expression string.
        Example: "2 + 3 * (4 - 1)" or "x * 5" after x = 3
        Should handle parentheses and variable substitution.
        """
        # Replace variables with their values
        for var, val in self.variables.items():
            expr = expr.replace(var, str(val))
        
        # Safe evaluation of mathematical expressions
        try:
            # Remove any characters that are not digits, operators, parentheses, or whitespace
            allowed_chars = re.compile(r'[0-9+\-*/(). ]')
            cleaned_expr = ''.join(filter(allowed_chars.match, expr))
            
            # Evaluate the expression
            result = eval(cleaned_expr)
            return result
        except ZeroDivisionError:
            return "Error: Division by zero"
        except Exception:
            return "Error: Invalid expression"

    def sqrt(self, x):
        """Return the square root of x."""
        if x < 0:
            return "Error: Cannot take square root of negative number"
        return math.sqrt(x)

    def power(self, base, exp):
        """Return base raised to the power of exp."""
        return base ** exp

    def factorial(self, n):
        """Return factorial of n."""
        if n < 0:
            return "Error: Factorial of negative number is undefined"
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)


if __name__ == "__main__":
    calc = Calculator()
    # Example: tests your agent should make pass
    print(calc.add(2, 3))            # Expect 5
    print(calc.divide(10, 0))        # Expect "Error: Division by zero"
    print(calc.evaluate_expression("2 + 3 * (4 - 1)"))  # Expect 11
    calc.assign_variable("x", 7)
    print(calc.evaluate_expression("x * 2"))  # Expect 14
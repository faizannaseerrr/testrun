import math
import re

class Calculator:
    def __init__(self):
        # Stores variables and memory operations
        self.memory = 0
        self.variables = {}

    def add(self, a, b):
        """Add two numbers."""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            return "Error: Invalid input"
        return a + b

    def subtract(self, a, b):
        """Subtract b from a."""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            return "Error: Invalid input"
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers."""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            return "Error: Invalid input"
        return a * b

    def divide(self, a, b):
        """Divide a by b, handle divide-by-zero gracefully."""
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            return "Error: Invalid input"
        if b == 0:
            return "Error: Division by zero"
        return a / b

    def store_in_memory(self, value):
        """Store a number in memory."""
        if not isinstance(value, (int, float)):
            return "Error: Invalid input"
        self.memory = value
        return f"Stored {value} in memory"

    def recall_memory(self):
        """Return the last stored value."""
        return self.memory

    def clear_memory(self):
        """Clear the stored memory value."""
        self.memory = 0
        return "Memory cleared"

    def assign_variable(self, name, value):
        """Assign a variable (like x = 5)."""
        if not isinstance(name, str) or not name.isalpha():
            return "Error: Invalid variable name"
        if not isinstance(value, (int, float)):
            return "Error: Invalid value"
        self.variables[name] = value
        return f"Assigned {name} = {value}"

    def evaluate_expression(self, expr):
        """
        Evaluate a mathematical expression string.
        Example: "2 + 3 * (4 - 1)" or "x * 5" after x = 3
        Should handle parentheses and variable substitution.
        """
        try:
            # Replace variables with their values
            for var, val in self.variables.items():
                expr = expr.replace(var, str(val))
            
            # Validate expression (only allow digits, operators, parentheses, and spaces)
            if not re.match(r'^[\d+\-*/(). ]+$', expr):
                return "Error: Invalid expression"
            
            # Additional validation to prevent multiple operators in a row
            if re.search(r'[+\-*/]{2,}', expr.replace(' ', '')):
                return "Error: Invalid expression"
            
            # Evaluate the expression
            result = eval(expr)
            return result
        except ZeroDivisionError:
            return "Error: Division by zero"
        except Exception:
            return "Error: Invalid expression"

    def sqrt(self, x):
        """Return the square root of x."""
        if not isinstance(x, (int, float)):
            return "Error: Invalid input"
        if x < 0:
            return "Error: Cannot take square root of negative number"
        return math.sqrt(x)

    def power(self, base, exp):
        """Return base raised to the power of exp."""
        if not isinstance(base, (int, float)) or not isinstance(exp, (int, float)):
            return "Error: Invalid input"
        try:
            return base ** exp
        except OverflowError:
            return "Error: Result too large"

    def factorial(self, n):
        """Return factorial of n."""
        if not isinstance(n, int):
            return "Error: Invalid input"
        if n < 0:
            return "Error: Factorial of negative number is undefined"
        if n > 1000:  # Prevent stack overflow
            return "Error: Number too large"
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
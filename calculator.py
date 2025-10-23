import math
import re

class Calculator:
    def __init__(self):
        # Stores variables and memory operations
        self.memory = 0
        self.variables = {}

    def add(self, a, b):
        """Add two numbers."""
        try:
            return a + b
        except TypeError:
            return "Error: Invalid input types for addition"

    def subtract(self, a, b):
        """Subtract b from a."""
        try:
            return a - b
        except TypeError:
            return "Error: Invalid input types for subtraction"

    def multiply(self, a, b):
        """Multiply two numbers."""
        try:
            # Check if inputs are valid numbers
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                raise TypeError
            return a * b
        except TypeError:
            return "Error: Invalid input types for multiplication"

    def divide(self, a, b):
        """Divide a by b, handle divide-by-zero gracefully."""
        try:
            if b == 0:
                return "Error: Division by zero"
            return a / b
        except TypeError:
            return "Error: Invalid input types for division"

    def store_in_memory(self, value):
        """Store a number in memory."""
        try:
            self.memory = float(value)
            return self.memory
        except (ValueError, TypeError):
            return "Error: Invalid value for memory storage"

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
        try:
            self.variables[name] = float(value)
            return f"{name} = {self.variables[name]}"
        except (ValueError, TypeError):
            return "Error: Invalid value for variable assignment"

    def evaluate_expression(self, expr):
        """
        Evaluate a mathematical expression string.
        Example: "2 + 3 * (4 - 1)" or "x * 5" after x = 3
        Should handle parentheses and variable substitution.
        """
        try:
            # Replace variables with their values
            processed_expr = expr
            for var, value in self.variables.items():
                processed_expr = processed_expr.replace(var, str(value))
            
            # Validate expression (only allow numbers, operators, parentheses, and spaces)
            if not re.match(r'^[0-9+\-*/(). ]+$', processed_expr):
                return "Error: Invalid characters in expression"
            
            # Evaluate the expression
            result = eval(processed_expr)
            return result
        except ZeroDivisionError:
            return "Error: Division by zero"
        except Exception as e:
            return f"Error: Invalid expression"

    def sqrt(self, x):
        """Return the square root of x."""
        try:
            if x < 0:
                return "Error: Cannot take square root of negative number"
            return math.sqrt(x)
        except TypeError:
            return "Error: Invalid input type for square root"

    def power(self, base, exp):
        """Return base raised to the power of exp."""
        try:
            # Check if inputs are valid numbers
            if not isinstance(base, (int, float)) or not isinstance(exp, (int, float)):
                raise TypeError
            return base ** exp
        except TypeError:
            return "Error: Invalid input types for power"

    def factorial(self, n):
        """Return factorial of n."""
        try:
            # Check if input is a valid number first
            if not isinstance(n, (int, float)):
                return "Error: Invalid input type for factorial"
            if n < 0:
                return "Error: Factorial is not defined for negative numbers"
            if not isinstance(n, int):
                return "Error: Factorial is only defined for integers"
            if n == 0 or n == 1:
                return 1
            return n * self.factorial(n - 1)
        except RecursionError:
            return "Error: Number too large for factorial calculation"


if __name__ == "__main__":
    calc = Calculator()
    # Example: tests your agent should make pass
    print(calc.add(2, 3))            # Expect 5
    print(calc.divide(10, 0))        # Expect "Error: Division by zero"
    print(calc.evaluate_expression("2 + 3 * (4 - 1)"))  # Expect 11
    calc.assign_variable("x", 7)
    print(calc.evaluate_expression("x * 2"))  # Expect 14
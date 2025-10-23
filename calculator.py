class Calculator:
    def __init__(self):
        # Stores variables and memory operations
        self.memory = 0
        self.variables = {}

    def add(self, a, b):
        """Add two numbers."""
        # TODO: Implement this
        pass

    def subtract(self, a, b):
        """Subtract b from a."""
        # TODO: Implement this
        pass

    def multiply(self, a, b):
        """Multiply two numbers."""
        # TODO: Implement this
        pass

    def divide(self, a, b):
        """Divide a by b, handle divide-by-zero gracefully."""
        # TODO: Implement this
        pass

    def store_in_memory(self, value):
        """Store a number in memory."""
        # TODO: Implement this
        pass

    def recall_memory(self):
        """Return the last stored value."""
        # TODO: Implement this
        pass

    def clear_memory(self):
        """Clear the stored memory value."""
        # TODO: Implement this
        pass

    def assign_variable(self, name, value):
        """Assign a variable (like x = 5)."""
        # TODO: Implement this
        pass

    def evaluate_expression(self, expr):
        """
        Evaluate a mathematical expression string.
        Example: "2 + 3 * (4 - 1)" or "x * 5" after x = 3
        Should handle parentheses and variable substitution.
        """
        # TODO: Implement safely (without eval)
        pass

    def sqrt(self, x):
        """Return the square root of x."""
        # TODO: Implement this
        pass

    def power(self, base, exp):
        """Return base raised to the power of exp."""
        # TODO: Implement this
        pass

    def factorial(self, n):
        """Return factorial of n."""
        # TODO: Implement recursively
        pass


if __name__ == "__main__":
    calc = Calculator()
    # Example: tests your agent should make pass
    print(calc.add(2, 3))            # Expect 5
    print(calc.divide(10, 0))        # Expect "Error: Division by zero"
    print(calc.evaluate_expression("2 + 3 * (4 - 1)"))  # Expect 11
    calc.assign_variable("x", 7)
    print(calc.evaluate_expression("x * 2"))  # Expect 14

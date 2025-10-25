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

    def _tokenize(self, expr):
        """Convert expression string into tokens."""
        # Remove spaces
        expr = expr.replace(" ", "")
        # Add spaces around operators and parentheses
        expr = re.sub(r'([+\-*/()^])', r' \1 ', expr)
        # Split and filter out empty strings
        tokens = [token for token in expr.split() if token]
        return tokens

    def _infix_to_postfix(self, tokens):
        """Convert infix notation to postfix using Shunting Yard algorithm."""
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        right_associative = {'^'}
        output = []
        operator_stack = []

        for token in tokens:
            if token.replace('.', '', 1).isdigit() or token.replace('-', '', 1).replace('.', '', 1).isdigit():
                output.append(float(token))
            elif token in self.variables:
                output.append(float(self.variables[token]))
            elif token in precedence:
                while (operator_stack and 
                       operator_stack[-1] != '(' and
                       operator_stack[-1] in precedence and
                       (precedence[operator_stack[-1]] > precedence[token] or
                        (precedence[operator_stack[-1]] == precedence[token] and token not in right_associative))):
                    output.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                if operator_stack and operator_stack[-1] == '(':
                    operator_stack.pop()  # Remove the '('
                else:
                    raise ValueError("Mismatched parentheses")

        while operator_stack:
            if operator_stack[-1] in '()':
                raise ValueError("Mismatched parentheses")
            output.append(operator_stack.pop())

        return output

    def _evaluate_postfix(self, postfix_tokens):
        """Evaluate postfix expression."""
        stack = []
        for token in postfix_tokens:
            if isinstance(token, float):
                stack.append(token)
            elif token == '+':
                if len(stack) < 2:
                    raise ValueError("Invalid expression")
                b, a = stack.pop(), stack.pop()
                stack.append(self.add(a, b))
            elif token == '-':
                if len(stack) < 2:
                    raise ValueError("Invalid expression")
                b, a = stack.pop(), stack.pop()
                stack.append(self.subtract(a, b))
            elif token == '*':
                if len(stack) < 2:
                    raise ValueError("Invalid expression")
                b, a = stack.pop(), stack.pop()
                stack.append(self.multiply(a, b))
            elif token == '/':
                if len(stack) < 2:
                    raise ValueError("Invalid expression")
                b, a = stack.pop(), stack.pop()
                result = self.divide(a, b)
                if isinstance(result, str):  # Error message
                    raise ValueError(result)
                stack.append(result)
            elif token == '^':
                if len(stack) < 2:
                    raise ValueError("Invalid expression")
                b, a = stack.pop(), stack.pop()
                stack.append(self.power(a, b))
            else:
                raise ValueError(f"Unknown token: {token}")
        
        if len(stack) != 1:
            raise ValueError("Invalid expression")
        return stack[0]

    def evaluate_expression(self, expr):
        """
        Evaluate a mathematical expression string.
        Example: "2 + 3 * (4 - 1)" or "x * 5" after x = 3
        Should handle parentheses and variable substitution.
        """
        try:
            tokens = self._tokenize(expr)
            postfix = self._infix_to_postfix(tokens)
            result = self._evaluate_postfix(postfix)
            return result
        except Exception as e:
            return f"Error: {str(e)}"

    def sqrt(self, x):
        """Return the square root of x."""
        if x < 0:
            return "Error: Cannot take square root of negative number"
        return math.sqrt(x)

    def power(self, base, exp):
        """Return base raised to the power of exp."""
        try:
            return base ** exp
        except OverflowError:
            return "Error: Result too large"

    def factorial(self, n):
        """Return factorial of n."""
        if not isinstance(n, int):
            return "Error: Factorial is only defined for integers"
        if n < 0:
            return "Error: Factorial is not defined for negative numbers"
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
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
        
        # Remove spaces
        expr = expr.replace(' ', '')
        
        try:
            # Use a safe evaluation method
            return self._evaluate(expr)
        except:
            return "Error: Invalid expression"
    
    def _evaluate(self, expr):
        # Handle parentheses first
        while '(' in expr:
            # Find the innermost parentheses
            start = -1
            for i, char in enumerate(expr):
                if char == '(':
                    start = i
                elif char == ')':
                    if start == -1:
                        raise ValueError("Mismatched parentheses")
                    # Evaluate the expression inside the parentheses
                    inner_expr = expr[start+1:i]
                    result = self._evaluate_simple(inner_expr)
                    expr = expr[:start] + str(result) + expr[i+1:]
                    break
        return self._evaluate_simple(expr)
    
    def _evaluate_simple(self, expr):
        # Handle multiplication and division
        tokens = re.split(r'(\*|/)', expr)
        i = 1
        while i < len(tokens):
            if tokens[i] == '*':
                result = self.multiply(float(tokens[i-1]), float(tokens[i+1]))
                tokens = tokens[:i-1] + [str(result)] + tokens[i+2:]
            elif tokens[i] == '/':
                result = self.divide(float(tokens[i-1]), float(tokens[i+1]))
                if isinstance(result, str):  # Error case
                    raise ValueError(result)
                tokens = tokens[:i-1] + [str(result)] + tokens[i+2:]
            else:
                i += 2
        
        # Handle addition and subtraction
        i = 1
        while i < len(tokens):
            if tokens[i] == '+':
                result = self.add(float(tokens[i-1]), float(tokens[i+1]))
                tokens = tokens[:i-1] + [str(result)] + tokens[i+2:]
            elif tokens[i] == '-':
                result = self.subtract(float(tokens[i-1]), float(tokens[i+1]))
                tokens = tokens[:i-1] + [str(result)] + tokens[i+2:]
            else:
                i += 2
        
        return float(tokens[0])

    def sqrt(self, x):
        """Return the square root of x."""
        if x < 0:
            return "Error: Cannot take square root of negative number"
        return math.sqrt(x)

    def power(self, base, exp):
        """Return base raised to the power of exp."""
        try:
            return base ** exp
        except:
            return "Error: Invalid power operation"

    def factorial(self, n):
        """Return factorial of n."""
        if not isinstance(n, int) or n < 0:
            return "Error: Factorial is only defined for non-negative integers"
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)


class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
    
    def print_board(self):
        print("\n  0 1 2")
        for i, row in enumerate(self.board):
            print(i, "|".join(row))
            if i < 2:
                print("  -+-+-")
    
    def make_move(self, row, col):
        if row < 0 or row > 2 or col < 0 or col > 2:
            return "Error: Position out of bounds"
        if self.board[row][col] != ' ':
            return "Error: Position already taken"
        
        self.board[row][col] = self.current_player
        return None
    
    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        
        # Check for tie
        for row in self.board:
            if ' ' in row:
                return None  # Game continues
        
        return 'Tie'
    
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def play(self):
        print("Welcome to Tic-Tac-Toe!")
        print("Enter moves as row,col (0-2)")
        
        while True:
            self.print_board()
            print(f"Player {self.current_player}'s turn")
            
            try:
                move = input("Enter row,col: ").strip()
                if move.lower() == 'quit':
                    print("Game exited")
                    break
                    
                row, col = map(int, move.split(','))
                error = self.make_move(row, col)
                
                if error:
                    print(error)
                    continue
                    
                winner = self.check_winner()
                if winner:
                    self.print_board()
                    if winner == 'Tie':
                        print("It's a tie!")
                    else:
                        print(f"Player {winner} wins!")
                    break
                    
                self.switch_player()
            except (ValueError, IndexError):
                print("Invalid input. Please enter row,col as two numbers between 0-2.")
            except KeyboardInterrupt:
                print("\nGame interrupted")
                break


if __name__ == "__main__":
    # Calculator tests
    calc = Calculator()
    print(calc.add(2, 3))            # Expect 5
    print(calc.divide(10, 0))        # Expect "Error: Division by zero"
    print(calc.evaluate_expression("2 + 3 * (4 - 1)"))  # Expect 11
    calc.assign_variable("x", 7)
    print(calc.evaluate_expression("x * 2"))  # Expect 14
    
    # Uncomment to play Tic-Tac-Toe
    # game = TicTacToe()
    # game.play()
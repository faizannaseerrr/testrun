# Simple Snake Game CLI Implementation
# Author: Assistant
# To run: python snake_game.py
# 
# Controls:
#   W - Move Up
#   A - Move Left
#   S - Move Down
#   D - Move Right
#   Q - Quit Game
#
# Game Rules:
# - Eat food (F) to grow your snake (O)
# - Avoid hitting walls or yourself
# - Your score increases with each food eaten

import random
import time
import os
class SnakeGame:
    def __init__(self, width=20, height=10):
        self.width = width
        self.height = height
        self.snake = [(height // 2, width // 2)]
        self.food = self._generate_food()
        self.direction = 'RIGHT'
        self.game_over = False

    def _generate_food(self):
        while True:
            food = (random.randint(0, self.height - 1), random.randint(0, self.width - 1))
            if food not in self.snake:
                return food

    def _move_snake(self):
        head_y, head_x = self.snake[0]
        
        if self.direction == 'UP':
            new_head = (head_y - 1, head_x)
        elif self.direction == 'DOWN':
            new_head = (head_y + 1, head_x)
        elif self.direction == 'LEFT':
            new_head = (head_y, head_x - 1)
        elif self.direction == 'RIGHT':
            new_head = (head_y, head_x + 1)
        
        # Check for collisions with walls
        if (new_head[0] < 0 or new_head[0] >= self.height or 
            new_head[1] < 0 or new_head[1] >= self.width):
            self.game_over = True
            return
        
        # Check for collision with self
        if new_head in self.snake:
            self.game_over = True
            return
        
        self.snake.insert(0, new_head)
        
        # Check if food is eaten
        if new_head == self.food:
            self.food = self._generate_food()
        else:
            self.snake.pop()

    def change_direction(self, direction):
        # Prevent 180-degree turns
        if (direction == 'UP' and self.direction != 'DOWN' or
            direction == 'DOWN' and self.direction != 'UP' or
            direction == 'LEFT' and self.direction != 'RIGHT' or
            direction == 'RIGHT' and self.direction != 'LEFT'):
            self.direction = direction

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Create the game board
        board = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        
        # Place snake on board
        for segment in self.snake:
            board[segment[0]][segment[1]] = 'O'
        
        # Place food on board
        board[self.food[0]][self.food[1]] = 'F'
        
        # Print the board
        print('+' + '-' * self.width + '+')
        for row in board:
            print('|' + ''.join(row) + '|')
        print('+' + '-' * self.width + '+')
        
        # Print score
        print(f"Score: {len(self.snake) - 1}")

    def run(self):
        print("Welcome to Snake Game!")
        print("Use WASD keys to control the snake. Press 'Q' to quit.")
        time.sleep(2)
        
        while not self.game_over:
            self.display()
            
            # Get user input
            try:
                user_input = input("Enter move (WASD): ").upper()
            except EOFError:
                # Handle non-interactive environments
                break
            
            if user_input == 'Q':
                break
            elif user_input == 'W':
                self.change_direction('UP')
            elif user_input == 'S':
                self.change_direction('DOWN')
            elif user_input == 'A':
                self.change_direction('LEFT')
            elif user_input == 'D':
                self.change_direction('RIGHT')
            
            self._move_snake()
            time.sleep(0.2)
        
        if self.game_over:
            print("Game Over!")
        print(f"Final Score: {len(self.snake) - 1}")


def main():
    game = SnakeGame()
    game.run()


if __name__ == "__main__":
    main()
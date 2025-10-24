import sys

class PingPongGame:
    def __init__(self):
        self.player1_score = 0
        self.player2_score = 0
        self.current_player = 1
        self.game_over = False

    def display_instructions(self):
        print("\nWelcome to Ping Pong CLI Game!")
        print("Player 1: Press '1' to hit the ball")
        print("Player 2: Press '2' to hit the ball")
        print("First player to reach 5 points wins!")
        print("Type 'quit' to exit the game")
        print("-" * 30)

    def display_score(self):
        print(f"\nScore - Player 1: {self.player1_score} | Player 2: {self.player2_score}")

    def switch_player(self):
        self.current_player = 2 if self.current_player == 1 else 1

    def hit_ball(self, player):
        if player == self.current_player:
            if player == 1:
                self.player1_score += 1
            else:
                self.player2_score += 1
            
            # Check for winner
            if self.player1_score >= 5:
                print("\nPlayer 1 wins the game!")
                self.game_over = True
            elif self.player2_score >= 5:
                print("\nPlayer 2 wins the game!")
                self.game_over = True
            else:
                self.switch_player()
                print(f"\nPlayer {player} scores a point!")
        else:
            print(f"\nPlayer {player} hit the ball out of turn! No point scored.")
            # Don't switch player when hitting out of turn
            # Player loses their turn but current player stays the same

    def play(self):
        self.display_instructions()
        
        while not self.game_over:
            self.display_score()
            print(f"Player {self.current_player}'s turn to hit the ball.")
            
            user_input = input("Hit the ball (1 for Player 1, 2 for Player 2) or 'quit' to exit: ").strip()
            
            if user_input.lower() == 'quit':
                print("\nThanks for playing!")
                sys.exit(0)
            
            if user_input == '1':
                self.hit_ball(1)
            elif user_input == '2':
                self.hit_ball(2)
            else:
                print("Invalid input. Please enter '1', '2', or 'quit'.")

if __name__ == "__main__":
    game = PingPongGame()
    game.play()
# Simple Tic-Tac-Toe game in Python
class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

    def play_game(self):
        while True:
            self.print_board()
            
            # Get player move
            print(f"{self.current_player} player's turn")
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
            
            # Check if move is valid
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid move! Try again.")
                continue

            # check if spot is taken
            if self.board[row][col] == " ":
                self.board[row][col] = self.current_player
            else:
                print("That spot is taken! Try again.")
                continue
            
            # Check for winner
            if self.check_winner():
                self.print_board()
                print(f"Player {self.current_player} wins!")
                break
            
            # Check for tie
            if all(self.board[i][j] != " " for i in range(3) for j in range(3)):
                self.print_board()
                print("It's a tie!")
                break
            
            # Switch players
            self.current_player = "O" if self.current_player == "X" else "X"

    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * 9)

    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != " ":
                return True
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                return True
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        
        return False
    
def main():
    # Start the game
    print("Welcome to Tic-Tac-Toe!")
    game = TicTacToe()
    game.play_game()

if __name__ == "__main__":
    main()
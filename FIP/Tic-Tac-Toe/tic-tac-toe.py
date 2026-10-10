import random

# Define the game board
board = [" "] * 9
ai_memory = {}

def display_board():
    print()
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i + 3]))
        if i < 6:
            print("--+---+--")
    print()

# Check if a player has won
def check_winner(player):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    return any(
        board[a] == board[b] == board[c] == player
        for a, b, c in winning_combinations
    )

# Check if the game is a tie
def check_tie():
    return " " not in board

# AI chooses a move using its experience
def ai_move():
    available = [i for i in range(9) if board[i] == " "]

    # Prefer moves that have worked well in previous games
    scores = [ai_memory.get(i, 0) for i in available]
    best_score = max(scores)
    best_moves = [
        move for move in available
        if ai_memory.get(move, 0) == best_score
    ]

    move = random.choice(best_moves)
    board[move] = "O"
    return move

# Main game loop
def main():
    global board

    print("Welcome to Tic-Tac-Toe!")
    print("You are X. The AI is O.")
    print("Enter a number from 1 to 9 to choose a square.")

    while True:
        board = [" "] * 9
        ai_moves = []

        while True:
            display_board()

            try:
                position = int(input("Choose a position (1-9): ")) - 1

                if position < 0 or position > 8 or board[position] != " ":
                    print("Invalid or occupied position. Try again.")
                    continue
            except ValueError:
                print("Please enter a number.")
                continue

            board[position] = "X"

            if check_winner("X"):
                display_board()
                print("You win!")
                for move in ai_moves:
                    ai_memory[move] = ai_memory.get(move, 0) - 1
                break

            if check_tie():
                display_board()
                print("It's a tie!")
                break

            move = ai_move()
            ai_moves.append(move)

            if check_winner("O"):
                display_board()
                print("AI wins!")
                for move in ai_moves:
                    ai_memory[move] = ai_memory.get(move, 0) + 1
                break

            if check_tie():
                display_board()
                print("It's a tie!")
                break

        again = input("Play again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing!")
            break

# Call the main game loop
if __name__ == "__main__":
    main()



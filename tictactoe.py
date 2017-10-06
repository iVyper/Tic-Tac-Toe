#!/usr/bin/env python3
"""
Tic Tac Toe Game in Python
This script allows two players to play a game of Tic Tac Toe from the command line.
"""


def print_board(board):
    """
    Displays the current game board in a human-readable format.

    Parameters:
        board (list): A list of 9 elements representing the board.
    """
    print("\n")
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print("\n")


def check_win(board, player):
    """
    Checks if the given player has won the game.

    Parameters:
        board (list): The current game board.
        player (str): The player's marker ('X' or 'O').

    Returns:
        bool: True if the player wins; otherwise, False.
    """
    win_conditions = [
        [0, 1, 2],  # Top row.
        [3, 4, 5],  # Middle row.
        [6, 7, 8],  # Bottom row.
        [0, 3, 6],  # Left column.
        [1, 4, 7],  # Middle column.
        [2, 5, 8],  # Right column.
        [0, 4, 8],  # Diagonal from top-left.
        [2, 4, 6]  # Diagonal from top-right.
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False


def check_tie(board):
    """
    Checks if the game has resulted in a tie.

    Parameters:
        board (list): The current game board.

    Returns:
        bool: True if all board cells are filled; otherwise, False.
    """
    return " " not in board


def main():
    """
    Main function to execute the game loop.
    Handles player input, move validation, and checks for game termination conditions.
    """
    # Initialize the board with empty spaces.
    board = [" " for _ in range(9)]
    current_player = "X"  # 'X' starts the game.

    while True:
        print_board(board)

        # Prompt current player for a move.
        try:
            move = int(input(f"Player {current_player}, choose your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid move. Please choose a number between 1 and 9.")
                continue
            move_index = move - 1  # Adjust for 0-based indexing.
            if board[move_index] != " ":
                print("That space is already taken. Please choose another move.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        # Make the move.
        board[move_index] = current_player

        # Check for a win.
        if check_win(board, current_player):
            print_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            break

        # Check for a tie.
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch the player.
        current_player = "O" if current_player == "X" else "X"

    # Offer the option to play again.
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again in ["yes", "y"]:
        main()  # Restart the game.
    else:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()

# Tic Tac Toe Game in Python

This is a simple command-line Tic Tac Toe game implemented in Python for two players. It allows two users to take turns and place their marks on the board, checks for win conditions or ties, and offers an option to play again.

## Features

- **Two-Player Gameplay:** Players alternate turns to mark their positions.
- **Win/Tie Detection:** Automatically checks for winning conditions or a tie after each move.
- **Input Validation:** Ensures moves are valid and that the selected space is not already taken.
- **Replay Option:** Offers the ability to restart the game after completion.

## Getting Started

### Prerequisites

- Python 3.x must be installed on your system.

### How to Run

1. **Clone the repository or download the `tictactoe.py` file.**

2. **Open your terminal or command prompt** and navigate to the directory containing the file.

3. **Run the game:**

   ```bash
   python3 tictactoe.py

4. **Follow the on-screen instructions to play.**

## Code Overview

- **print_board(board):** Displays the current state of the board.
- **check_win(board, player):** Checks if a player has won by completing a row, column, or diagonal.
- **check_tie(board):** Checks if the board is full and the game is a draw.
- **main():** Orchestrates the game flow, alternating turns and checking for win/draw conditions.

## License

This project is open-source and available under the MIT License.
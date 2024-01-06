# Tic Tac Toe Game (TickTacToe)

## Overview

This Python project is a simple implementation of the classic Tic Tac Toe game, where two players take turns to mark 'X' or 'O' on a 3x3 grid. The game checks for a winner after each move and prints the current state of the board.

## Functions

### `sum(lst)`

Calculates the sum of the elements in the given list `lst`.

### `check_win(xState, zState)`

Checks for a winning condition on the Tic Tac Toe board. It examines all possible winning combinations and returns the winner (1 for 'X', 0 for 'O') or -1 if there is no winner yet.

### `printboard(xState, zState)`

Prints the current state of the Tic Tac Toe board, displaying 'X' or 'O' for filled positions and the position number for empty spots.

## Usage

1. Run the script:

   ```bash
   python your_script_name.py
Follow the on-screen instructions to play the game. Players take turns entering the position number where they want to place their 'X' or 'O'.

The game checks for a winner after each move and displays the current state of the board.

The game continues until there is a winner or a draw.

Notes
The game assumes two players taking turns, with 'X' going first.

The board positions are numbered from 0 to 8 as follows:

| 0 | 1 | 2 |
| 3 | 4 | 5 |
| 6 | 7 | 8 |


Customization
You can modify the printboard function to customize the display of the board.
Extend the game logic or add additional features based on your preferences.
Credits
[Harsh Chainani]






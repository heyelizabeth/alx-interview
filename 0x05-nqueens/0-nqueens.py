#!/usr/bin/python3
"""
Module to solve the N Queens problem.
"""

# Importing sys module to handle command-line arguments and exit.
import sys


def is_safe(board, row, col):
    """
    Check if a queen can be placed on board at (row, col).
    This function checks the column and the diagonals.

    Args:
        board (list): The current board state.
        row (int): Row index to check.
        col (int): Column index to check.

    Returns:
        bool: True if the position is safe, False otherwise.
    """
    # Check this column on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, col, solutions):
    """
    Use backtracking to find all solutions for the N Queens problem.

    Args:
        board (list): The current board state.
        col (int): Current column to place the queen.
        solutions (list): List to store all possible solutions.

    Returns:
        None
    """
    # If all queens are placed, add the solution to the list
    if col >= len(board):
        solution = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    # Try placing a queen in all rows in the current column
    for i in range(len(board)):
        if is_safe(board, i, col):  # Check if it's safe to place the queen
            board[i][col] = 1  # Place the queen
            solve_nqueens(board, col + 1, solutions)  # Recur to place the rest
            board[i][col] = 0  # Backtrack and remove the queen


def nqueens(N):
    """
    Initialize the board and call the solver function.

    Args:
        N (int): Size of the board (NxN) and number of queens.

    Returns:
        list: List of all possible solutions.
    """
    # Create an NxN board initialized with 0
    board = [[0] * N for _ in range(N)]
    solutions = []  # List to store all possible solutions
    solve_nqueens(board, 0, solutions)  # Start solving from the first column
    return solutions


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])  # Convert the input argument to an integer
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:  # Check if N is less than 4
        print("N must be at least 4")
        sys.exit(1)

    solutions = nqueens(N)  # Get all possible solutions for N queens

    for solution in solutions:
        print(solution)  # Print each solution

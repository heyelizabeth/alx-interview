#!/usr/bin/python3
import sys

# Handle input validation
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)


# Define the function to check if it's safe to place a queen
def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]"""
    # Check column
    for i in range(row):
        if board[i] == col:
            return False

    # Check diagonals
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


# Define the backtracking function to solve N Queens
def solve_nqueens(N):
    """Solve the N Queens problem and print all solutions"""
    def backtrack(row, board):
        if row == N:
            # If all queens are placed, print the board configuration
            print([[i, board[i]] for i in range(N)])
            return

        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1, board)
                board[row] = -1

    board = [-1] * N
    backtrack(0, board)


# Call the solver
solve_nqueens(N)

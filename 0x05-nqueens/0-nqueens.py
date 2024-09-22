#!/usr/bin/python3
""" N queens problem
"""
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    number_q = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    exit(1)

if number_q < 4:
    print("N must be at least 4")
    exit(1)


def solve_nqueens(number):
    """ solve n queens problem
    """
    if number == 0:
        return [[]]
    inner_solution = solve_nqueens(number - 1)
    return [solution + [(number, i + 1)]
            for i in range(number_q)
            for solution in inner_solution
            if safe_queen((number, i + 1), solution)]


def attack_queen(square, queen):
    """ check if queen is attacking another gouine
    """
    (first_row, first_col) = square
    (second_row, second_col) = queen
    return (first_row == second_row) or (first_col == second_col) or\
        abs(first_row - second_row) == abs(first_col - second_col)


def safe_queen(square, queens):
    """ check if queen is safe
    """
    for queen in queens:
        if attack_queen(square, queen):
            return False
    return True


for answer in reversed(solve_nqueens(number_q)):
    result = []
    for answer_list in [list(answer_list) for answer_list in answer]:
        result.append([i - 1 for i in answer_list])
    print(result)

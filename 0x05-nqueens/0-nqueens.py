#!/usr/bin/python3
"""
    The N queens puzzle is the challenge of placing N non-attacking queens
    on an N×N chessboard. Write a program that solves the N queens problem.
"""

import sys


def is_safe(board, row, col):
    for prev_row in range(row):
        if board[prev_row][col] == 1:
            return False
        col_diff = abs(col - board[prev_row].index(1))
        row_diff = abs(row - prev_row)
        if col_diff == row_diff:
            return False
    return True


def solve_nqueens(n):
    solutions = []
    board = [[0] * n for _ in range(n)]

    def backtrack(row):
        if row == n:
            solutions.append([[i, board[i].index(1)] for i in range(n)])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                backtrack(row + 1)
                board[row][col] = 0
    backtrack(0)
    return solutions


def print_solutions(solutions):
    for solution in solutions:
        print(solution)


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solutions = solve_nqueens(n)
    print_solutions(solutions)


if __name__ == "__main__":
    main()

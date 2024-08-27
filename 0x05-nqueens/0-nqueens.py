#!/usr/bin/python3

"""
N queens
"""

import sys


def is_safe(board, row, col, N):
    """
    Check if a queen can be placed on the board at the specified row and column
    without being attacked by any other queen.

    Args:
    board (list of list of int): The current state of the chessboard.
    row (int): The row where the queen is to be placed.
    col (int): The column where the queen is to be placed.
    N (int): The size of the chessboard.

    Returns:
    bool: True if it's safe to place the queen, False otherwise.
    """
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, N, solutions):
    """
    Solve the N queens problem by placing queens one by one
    in different columns.

    Args:
    board (list of list of int): The current state of the chessboard.
    col (int): The current column to place a queen.
    N (int): The size of the chessboard.
    solutions (list of list of list of int): The list to store
    all solutions found.

    Returns:
    bool: True if a solution is found, False otherwise.
    """
    # If all queens are placed, store the solution
    if col >= N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place the queen
            board[i][col] = 1

            # Recur to place the rest of the queens
            res = solve_nqueens_util(board, col + 1, N, solutions) or res

            # If placing queen doesn't lead to a solution, backtrack
            board[i][col] = 0

    return res


def solve_nqueens(N):
    """
    Initialize the chessboard and solve the N queens problem.

    Args:
    N (int): The size of the chessboard.

    Returns:
    list of list of list of int: A list containing all the solutions.
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)
    return solutions


def main():
    """
    Main function to handle command-line arguments and solve the
    N queens problem.
    """
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        # Convert the input argument to an integer
        N = int(sys.argv[1])
    except ValueError:
        # If the conversion fails, print an error message
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N queens problem
    solutions = solve_nqueens(N)

    # Print each solution in the required format
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()

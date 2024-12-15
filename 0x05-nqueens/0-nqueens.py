#!/usr/bin/python3
'''
A module to solve the n queens
'''

import sys


def print_solution(solution):
    """Prints a single solution in the required format."""
    print([[i, solution[i]] for i in range(len(solution))])


def solve_nqueens(n, row, solution, columns, diag1, diag2, results):
    """Recursive backtracking function to find all solutions."""
    if row == n:
        results.append(solution[:])
        return

    for col in range(n):
        if not columns[col] and not diag1[row + col] and not diag2[row - col + n - 1]:
            # Place the queen
            solution[row] = col
            columns[col] = diag1[row + col] = diag2[row - col + n - 1] = True

            # Recurse to the next row
            solve_nqueens(n, row + 1, solution, columns, diag1, diag2, results)

            # Backtrack
            solution[row] = -1
            columns[col] = diag1[row + col] = diag2[row - col + n - 1] = False


def nqueens(n):
    """Solves the N Queens problem and prints all solutions."""
    solution = [-1] * n  # -1 indicates no queen placed in the row yet
    results = []

    # Helper arrays to track column and diagonal conflicts
    columns = [False] * n
    diag1 = [False] * (2 * n - 1)
    diag2 = [False] * (2 * n - 1)

    solve_nqueens(n, 0, solution, columns, diag1, diag2, results)

    for res in results:
        print_solution(res)


if __name__ == "__main__":
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

    nqueens(N)

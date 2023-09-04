#!/usr/bin/python3
"""
N-queens puzzle  problem
Description: The N queens puzzle is the challenge of placing N non-attacking
queens on an N×N chessboard. Write a program that solves the N queens problem.
Usage: ./101-nqueens.py N
    If the user called the program with the wrong number of arguments,
    print Usage: nqueens N, followed by a new line, and exit with the status 1
    where N must be an integer greater or equal to 4
    If N is not an integer, print N must be a number, followed by a new line,
    and exit with the status 1
"""

import sys


def already_exists(y):
    """check that a queen does not already exist in that y value"""
    for x in range(n):
        if y == a[x][1]:
            return True
    return False


def reject(x, y):
    """determines whether or not to reject the solution"""
    if (already_exists(y)):
        return False
    i = 0
    while (i < x):
        if abs(a[i][1] - y) == abs(i - x):
            return False
        i += 1
    return True


def clear_a(x):
    """clears the answers from the point of failure on"""
    for i in range(x, n):
        a[i][1] = None


def nqueens(x):
    """recursive backtracking function to find the solution"""
    for y in range(n):
        clear_a(x)
        if reject(x, y):
            a[x][1] = y
            if (x == n - 1):  # accepts the solution
                print(a)
            else:
                nqueens(x + 1)


if __name__ == "__main__":
    """Solve the N queens problem"""

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    n = int(sys.argv[1])
    a = [[i, None] for i in range(n)]

    nqueens(0)

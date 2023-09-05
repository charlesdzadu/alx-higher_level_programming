#!/usr/bin/python3
""" Module that divides all elements of a matrix """


def matrix_divided(matrix, div):
    """ Function that divides all elements of a matrix

    Args:
        matrix (list): list of lists of integers or floats
        div (int): number to divide each element of the matrix
    Returns:
        list: list of lists of integers or floats

    Raises:
        TypeError: if matrix is not a list of lists of integers or floats
        TypeError: if each row of the matrix is not of the same size
        TypeError: if div is not an integer or float
        ZeroDivisionError: if div is equal to 0
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])

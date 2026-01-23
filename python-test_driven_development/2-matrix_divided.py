#!/usr/bin/python3
# Divides all elements of a matrix by a given number with strict validation

"""Defines matrix_divided."""


def matrix_divided(matrix, div):
    """Divide all matrix elements by div and round to 2 decimals."""

    if (not isinstance(matrix, list) or len(matrix) == 0 or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_size = len(matrix[0])

    for row in matrix:
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if type(elem) not in (int, float):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of "
                    "integers/floats"
                )

    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]

#!/usr/bin/python3
# Prints a matrix of integers
def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    for row in matrix:
        if len(row) == 0:
            print()
            continue
        for i in range(len(row)):
            if i != len(row) - 1:
                print("{:d}".format(row[i]), end=" ")
            else:
                print("{:d}".format(row[i]))

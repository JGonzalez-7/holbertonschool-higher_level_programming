#!/usr/bin/python3
# Prints a square using the # character

"""Defines print_square(size)."""


def print_square(size):
    """Print a square of size x size using #."""

    if type(size) is bool:
        raise TypeError("size must be an integer")

    if type(size) is float:
        raise TypeError("size must be an integer")

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)

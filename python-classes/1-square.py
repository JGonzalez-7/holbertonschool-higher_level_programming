#!/usr/bin/python3
# Define a Square class with a private size attribute
"""Defines a Square class with a private size attribute."""


class Square:
    """Represents a square."""

    def __init__(self, size):
        """Initialize a Square instance.

        Args:
            size: The size of the square (no validation).
        """
        self.__size = size

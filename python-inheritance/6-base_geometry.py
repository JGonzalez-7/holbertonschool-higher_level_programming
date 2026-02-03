#!/usr/bin/python3
"""Module that defines a BaseGeometry class with area method."""


class BaseGeometry:
    """Base geometry class."""

    def area(self):
        """Raise an exception indicating area is not implemented."""
        raise Exception("area() is not implemented")

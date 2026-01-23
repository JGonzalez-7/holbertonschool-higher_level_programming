#!/usr/bin/python3
# Adds two integers after validating input types
"""Defines add_integer(a, b=98)."""


def add_integer(a, b=98):
    """Add two numbers after casting floats to ints."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)

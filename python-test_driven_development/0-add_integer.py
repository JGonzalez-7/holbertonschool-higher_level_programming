#!/usr/bin/python3
# Adds two integers after validating input types (handles NaN/inf)
"""Defines add_integer(a, b=98)."""


def add_integer(a, b=98):
    """Add two numbers after casting floats to ints."""

    def _check_num(x, name):
        if not isinstance(x, (int, float)):
            raise TypeError(f"{name} must be an integer")

        # Reject NaN and infinities (they break int() casting)
        if isinstance(x, float):
            if x != x:  # NaN check
                raise TypeError(f"{name} must be an integer")
            if x == float("inf") or x == float("-inf"):  # Infinity check
                raise TypeError(f"{name} must be an integer")

        return int(x)

    return _check_num(a, "a") + _check_num(b, "b")

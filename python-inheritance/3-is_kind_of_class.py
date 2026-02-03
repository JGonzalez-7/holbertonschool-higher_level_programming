#!/usr/bin/python3
"""Module to check instance or inherited class."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or its subclasses."""
    return isinstance(obj, a_class)

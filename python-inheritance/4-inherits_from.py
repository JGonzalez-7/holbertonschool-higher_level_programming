#!/usr/bin/python3
"""Module to check subclass inheritance."""


def inherits_from(obj, a_class):
    """Return True if obj inherits from a_class but is not exactly a_class."""
    return isinstance(obj, a_class) and type(obj) is not a_class

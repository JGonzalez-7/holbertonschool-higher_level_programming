#!/usr/bin/python3
# Replaces an element in a copy of a list
def new_in_list(my_list, idx, element):
    """Return a new list with one element replaced."""
    new_list = my_list.copy()

    if idx < 0 or idx >= len(my_list):
        return new_list

    new_list[idx] = element
    return new_list

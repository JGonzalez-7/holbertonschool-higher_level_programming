#!/usr/bin/python3
# Retrieves an element from a list safely
def element_at(my_list, idx):
    """Return the element at index idx, or None if invalid."""
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]

#!/usr/bin/python3
# Finds the biggest integer in a list
def max_integer(my_list=[]):
    """Return the maximum integer in a list, or None if the list is empty."""
    if not my_list:
        return None

    max_value = my_list[0]
    for num in my_list:
        if num > max_value:
            max_value = num

    return max_value

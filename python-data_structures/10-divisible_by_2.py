#!/usr/bin/python3
# Finds multiples of 2 in a list
def divisible_by_2(my_list=[]):
    """Return a list of booleans indicating if numbers are divisible by 2."""
    result = []

    for num in my_list:
        result.append(num % 2 == 0)

    return result

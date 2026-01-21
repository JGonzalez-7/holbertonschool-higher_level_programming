#!/usr/bin/python3
# Prints all integers of a list in reverse order
def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order."""
    for i in reversed(my_list):
        print("{}".format(i))

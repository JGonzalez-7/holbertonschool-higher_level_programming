#!/usr/bin/python3
# Prints all integers of a list, one per line
def print_list_integer(my_list=[]):
    """Print all integers of a list."""
    for i in my_list:
        print("{:d}".format(i))

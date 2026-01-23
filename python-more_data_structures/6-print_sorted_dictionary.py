#!/usr/bin/python3
# Print a dictionary with keys sorted in alphabetical order
def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))

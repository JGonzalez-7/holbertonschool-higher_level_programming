#!/usr/bin/python3
# Replace all occurrences of an element in a list with a new value
def search_replace(my_list, search, replace):
    return [replace if value == search else value for value in my_list]

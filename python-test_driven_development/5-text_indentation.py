#!/usr/bin/python3
# Prints text with two new lines after '.', '?' and ':'

"""Defines text_indentation(text)."""


def text_indentation(text):
    """Print text with two new lines after '.', '?' and ':'."""

    if type(text) is not str:
        raise TypeError("text must be a string")

    at_line_start = True

    for char in text:
        if char == " " and at_line_start:
            continue

        print(char, end="")

        if char in ".?:":
            print("\n")
            at_line_start = True
        else:
            at_line_start = False

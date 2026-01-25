#!/usr/bin/python3
# Prints text with indentation after specific punctuation

"""Defines text_indentation(text)."""


def text_indentation(text):
    """Print text with two new lines after ., ? and :."""

    if type(text) is not str:
        raise TypeError("text must be a string")

    line = ""
    for char in text:
        line += char
        if char in ".?:":
            print(line.strip())
            print()
            line = ""

    if line:
        print(line.strip(), end="")

#!/usr/bin/python3
# Print and return the last digit of a number

def print_last_digit(number):
    # Make the number positive to get the correct last digit
    last_digit = abs(number) % 10
    print("{}".format(last_digit), end="")
    return last_digit

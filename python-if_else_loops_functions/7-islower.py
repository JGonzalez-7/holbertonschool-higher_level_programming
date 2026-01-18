#!/usr/bin/python3
# Check if a character is lowercase using ASCII values

def islower(c):
    # ASCII range for lowercase letters: a (97) to z (122)
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    return False

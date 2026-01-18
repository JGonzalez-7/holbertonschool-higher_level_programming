#!/usr/bin/python3
# Print a string converted to uppercase using ASCII values

def uppercase(str):
    for c in str:
        # Convert lowercase letters to uppercase using ASCII math
        if ord(c) >= 97 and ord(c) <= 122:
            print("{:c}".format(ord(c) - 32), end="")
        else:
            print("{}".format(c), end="")
    print()

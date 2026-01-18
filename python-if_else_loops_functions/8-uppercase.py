#!/usr/bin/python3
# Print a string converted to uppercase using ASCII values

def uppercase(str):
    result = ""
    for c in str:
        # Convert lowercase letters to uppercase using ASCII math
        if ord(c) >= 97 and ord(c) <= 122:
            result += "{:c}".format(ord(c) - 32)
        else:
            result += "{}".format(c)
    print("{}".format(result))

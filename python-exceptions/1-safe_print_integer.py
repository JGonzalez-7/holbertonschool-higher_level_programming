#!/usr/bin/python3
# Safely prints an integer using try/except and format
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        return False

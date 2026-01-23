#!/usr/bin/python3
# Safely divides two integers and prints the result using finally
def safe_print_division(a, b):
    result = None

    try:
        result = a / b
        return result
    except Exception:
        return None
    finally:
        print("Inside result: {}".format(result))

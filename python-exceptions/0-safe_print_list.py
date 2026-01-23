#!/usr/bin/python3
# Prints x elements of a list safely using try/except
def safe_print_list(my_list=[], x=0):
    count = 0

    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except Exception:
            break

    print()
    return count

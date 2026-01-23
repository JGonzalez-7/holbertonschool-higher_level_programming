#!/usr/bin/python3
# Prints only integers from a list safely and counts them
def safe_print_list_integers(my_list=[], x=0):
    count = 0

    for i in range(x):
        try:
            value = my_list[i]
        except Exception:
            raise

        try:
            print("{:d}".format(value), end="")
            count += 1
        except Exception:
            continue

    print()
    return count

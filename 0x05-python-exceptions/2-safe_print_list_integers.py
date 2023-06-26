#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Prints a list of integers from my_list up to the specified count, x.
    """
    result = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            result += 1
        except (ValueError, TypeError):
            continue
    print()
    return result

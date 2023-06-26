#!/usr/bin/python3

def safe_print_division(a, b):
    """
    Divides two integers and prints the result.
    Catches division by zero exception.
    """
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result

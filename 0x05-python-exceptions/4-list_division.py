#!/usr/bin/python3

"""
Divides element by element between two lists.
"""


def list_division(my_list_1, my_list_2, list_length):
    result = []
    for x in range(list_length):
        try:
            result.append(my_list_1[x] / my_list_2[x])
        except IndexError:
            print("Out of range")
            result.append(0)
        except TypeError:
            print("Wrong type")
            result.append(0)
        except ZeroDivisionError:
            print("Division by 0")
            result.append(0)
        finally:
            pass
    return result


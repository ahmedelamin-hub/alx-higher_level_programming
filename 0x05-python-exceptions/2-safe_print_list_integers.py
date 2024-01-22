#!/bin/usr/python3

def safe_print_list_integers(my_list=[], x=0):
    t = 0
    for we in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            t += 1
        except (ValueError, TypeError, IndexError):
            if isinstance(my_list[we], IndexError):
                raise
            continue
    print()
    return t

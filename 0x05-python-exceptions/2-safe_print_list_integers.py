#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    t = 0
    try:
        for we in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                t += 1
            except (ValueError, TypeError, IndexError):
                continue
    except IndexError:
        pass
    print()
    return t

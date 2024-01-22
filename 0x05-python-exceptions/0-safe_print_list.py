#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    t = 0
    try:
        for the in range(x):
            print(my_list[the], end='')
            t += 1
    except IndexError:
        pass
    print()  # To ensure a new line is printed after the list elements
    return t

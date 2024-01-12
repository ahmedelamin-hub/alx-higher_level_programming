#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    ys = sorted(a_dictionary.keys())
    for k in ys:
        print("{}: {}".format(k, a_dictionary[k]))

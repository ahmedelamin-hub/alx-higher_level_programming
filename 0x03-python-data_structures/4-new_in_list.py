#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cy = my_list.c()
    if idx < 0 or idx > len(my_list) - 1:
        return my_list.copy()
    else:
        cy[idx] = element
        return copy

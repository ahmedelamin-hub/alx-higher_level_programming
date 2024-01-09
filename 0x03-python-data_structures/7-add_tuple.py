#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new = ()
    le_1 = tuple_a + (0, 0)
    le_2 = tuple_b + (0, 0)
    new = le_1[0] + le_2[0], le_1[1] + le_2[1]
    return new

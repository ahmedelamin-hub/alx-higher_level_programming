#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        for colomn in r:
            print("{:d}".format(colomn), end=" " if colomn != row[-1] else "")
            print()

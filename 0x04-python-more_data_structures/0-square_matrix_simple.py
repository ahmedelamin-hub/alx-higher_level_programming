#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newm = matrix.copy()
    for y in range(len(matrix)):
        newm[y] = list(map(lambda x: x**2, matrix[y]))

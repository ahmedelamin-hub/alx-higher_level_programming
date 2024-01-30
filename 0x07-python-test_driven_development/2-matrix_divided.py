#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor and rounds the results.

    Parameters:
    matrix (list of lists of int/float): The matrix to be divided.
    div (int/float): The divisor.

    Raises:
    TypeError: If the matrix is not a list of lists of integers/floats,
               if rows of the matrix are not of the same size,
               or if div is not a number.
    ZeroDivisionError: If div is zero.

    Returns:
    list of lists of float: New matrix with all values divided by div.
    """
    if not matrix or not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(elem, (int, float)) for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]

#!/usr/bin/python3
"""function for Pascal's Triangle."""i


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the n-th row.

    Args:
    n (int): The number of rows in Pascal's triangle to generate.

    Returns:
    List[List[int]]: A list of lists containing rows of Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle

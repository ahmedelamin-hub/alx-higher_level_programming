#!/usr/bin/python3


def add_integer(a, b=98):
    """
    Adds two numbers, a and b, where a is required and b is optional (default=98).
    Both a and b must be integers or floats. Floats are cast to integers.

    Raises:
        TypeError: if either a or b is neither an integer nor a float.

    Returns:
        int: The addition of a and b after casting them to integers.
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

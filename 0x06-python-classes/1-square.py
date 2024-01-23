#!/usr/bin/python3
"""
This module defines the Square class.
It represents a square with a private size attribute.
"""


class Square:
    """
    Represents a square with a private instance attribute: size.

    Attributes:
    size (int): The size of the square, not directly accessible.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
        size (int): The size of the square.
        """
        self.__size = size


if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)

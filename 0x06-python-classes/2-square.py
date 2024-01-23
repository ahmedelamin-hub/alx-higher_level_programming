#!/usr/bin/python3
"""
This module defines the Square class.
It represents a square with a private size attribute,
with added type and value checks.
"""


class Square:
    """
    Represents a square with a private instance attribute: size.
    Size must be an integer and greater than or equal to 0.

    Attributes:
    size (int): The size of the square, not directly accessible.
    """

    def __init__(self, size=0):

        """
        Initializes a new Square instance with a size.

        Args:
        size (int): The size of the square. Defaults to 0.

        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size


if __name__ == "__main__":

    my_square_1 = Square(3)
    print(type(my_square_1))
    print(my_square_1.__dict__)

    my_square_2 = Square()
    print(type(my_square_2))
    print(my_square_2.__dict__)

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    try:
        my_square_3 = Square("3")
        print(type(my_square_3))
        print(my_square_3.__dict__)
    except Exception as e:
        print(e)

    try:
        my_square_4 = Square(-89)
        print(type(my_square_4))
        print(my_square_4.__dict__)
    except Exception as e:
        print(e)

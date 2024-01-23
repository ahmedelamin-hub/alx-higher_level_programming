#!/usr/bin/python3
"""
This module defines the Square class.
It represents a square with a private size attribute and
a method to calculate its area.
"""

class Square:
    """
    Represents a square with a private instance attribute: size,
    and a method to calculate the square's area.

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

    def area(self):
        """
        Calculates the area of the square.

        Returns:
        The area of the square.
        """
        return self.__size ** 2

if __name__ == "__main__":
    my_square_1 = Square(3)
    print("Area: {}".format(my_square_1.area()))

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    my_square_2 = Square(5)
    print("Area: {}".format(my_square_2.area()))

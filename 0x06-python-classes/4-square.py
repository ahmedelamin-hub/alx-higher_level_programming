#!/usr/bin/python3
"""
This module defines the Square class.
It represents a square with a private size attribute, along with
getter and setter methods for size, and a method to calculate its area.
"""


class Square:

    """
    Represents a square with a private instance attribute: size.
    Provides a getter and setter for size with validation.

    Attributes:
    size (int): The size of the square, accessible through a property.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance with a size.

        Args:
        size (int): The size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Args:
        value (int): The new size of the square.

        Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
        The area of the square.
        """
        return self.__size ** 2


if __name__ == "__main__":

    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)

#!/usr/bin/python3
"""
This module defines the Square class.
It represents a square with a private size attribute, getter and setter for size,
a method to calculate its area, and a method to print the square using '#'.
"""

class Square:
    """
    Represents a square with a private instance attribute: size.
    Provides a getter and setter for size with validation, a method to calculate
    the square's area, and a method to print the square.

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

    def my_print(self):
        """
        Prints the square using the '#' character.
        If the size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

if __name__ == "__main__":
    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")

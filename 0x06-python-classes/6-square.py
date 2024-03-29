#!/usr/bin/python3
"""
This module defines the Square class.
It represents a square with private size and position attributes,
with getters and setters for each, a method to calculate its area,
and a method to print the square using '#', considering its position.
"""


class Square:
    """
    Represents a square with private instance attributes: size and position.
    Provides getters and setters for these attributes with validation

    Attributes:
    size (int): The size of the square, accessible through a property.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance with a size and position.

        Args:
        size (int): The size of the square. Defaults to 0.
        position (tuple): The position of the square. Defaults to (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square."""
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

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square with validation.

        Args:
        value (tuple): The new position of the square.

        Raises:
        TypeError: If the position is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of the square.."""
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the '#' character, considering its position.
        If the size is 0, prints an empty line.
        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)


if __name__ == "__main__":
    my_square_1 = Square(3)
    my_square_1.my_print()

    print("--")

    my_square_2 = Square(3, (1, 1))
    my_square_2.my_print()

    print("--")

    my_square_3 = Square(3, (3, 0))
    my_square_3.my_print()

    print("--")

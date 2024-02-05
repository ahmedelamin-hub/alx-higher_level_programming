#!/usr/bin/python3
"""Square class inheriting from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A representation of a square."""

    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
        size (int): The size of the square sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

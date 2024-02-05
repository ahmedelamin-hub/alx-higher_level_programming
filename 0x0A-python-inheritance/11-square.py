#!/usr/bin/python3
"""Defines Square class inheriting from Rectangle."""


class Square(Rectangle):
    """Representation of a square."""

    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
        size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the print() and str()"""
        return f"[Square] {self.__size}/{self.__size}"

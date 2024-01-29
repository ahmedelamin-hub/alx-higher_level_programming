#!/usr/bin/python3

class Rectangle:
    """A class that models a rectangle shape."""

    def __init__(self, rect_width=0, rect_height=0):
        """Constructs a Rectangle instance with specified width and height.

        Args:
            rect_width (int): The width dimension of the rectangle.
            rect_height (int): The height dimension of the rectangle.
        """
        self.rect_width = rect_width
        self.rect_height = rect_height

    @property
    def rect_width(self):
        """int: Retrieves the width of the rectangle."""
        return self.__width

    @rect_width.setter
    def rect_width(self, value):
        """Sets the width of the rectangle, ensuring it's valid.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is negative.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def rect_height(self):
        """int: Retrieves the height of the rectangle."""
        return self.__height

    @rect_height.setter
    def rect_height(self, value):
        """Sets the height of the rectangle, ensuring it's valid.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is negative.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

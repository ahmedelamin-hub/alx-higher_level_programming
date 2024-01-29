#!/usr/bin/python3

class Rectangle:
    """Class representing a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle with optional width and height.

        Args:
            width (int): The width of the rectangle, defaults to 0.
            height (int): The height of the rectangle, defaults to 0.
        """
        self.dimension_width = width
        self.dimension_height = height

    @property
    def width(self):
        """int: Retrieve the width of the rectangle."""
        return self.dimension_width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.dimension_width = value

    @property
    def height(self):
        """int: Retrieve the height of the rectangle."""
        return self.dimension_height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.dimension_height = value

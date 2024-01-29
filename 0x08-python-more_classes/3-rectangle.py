#!/usr/bin/python3

class Rectangle:
    """Class representing a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle, defaults to 0.
            height (int): The height of the rectangle, defaults to 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """int: Retrieve or set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: Retrieve or set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return the printable representation of the rectangle.

        Represents the rectangle with the character '#'.
        Returns an empty string if width or height is equal to 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        
        rect_lines = []
        for _ in range(self.__height):
            line = '#' * self.__width
            rect_lines.append(line)

        return '\n'.join(rect_lines)

    def __repr__(self):
        """Return the string representation of the rectangle."""
        return f"{self.__class__.__name__}({self.__width}, {self.__height})"

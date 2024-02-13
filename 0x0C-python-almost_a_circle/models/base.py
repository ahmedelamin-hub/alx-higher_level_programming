#!/usr/bin/python3
"""Module for the Base class."""


class Base:
    """Represents the base model.

    Attributes:
        __nb_objects (int): Number of created objects.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int): The identity of the instance

        Attributes:
            id (int): The identity of the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

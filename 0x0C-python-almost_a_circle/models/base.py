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
            id (int, optional): The identity

        Attributes:
            id (int): The identity of the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation"""
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation."""
        filename = cls.__name__ + ".json"
        list_dicts = ([obj.to_dictionary() for obj in list_objs]
                      if list_objs else [])
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list represented by json_string."""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes set."""
        dummy = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances from a file."""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                list_dicts = cls.from_json_string(file.read())
            return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

#!/usr/bin/python3
"""
This module defines the Student class with serialization/ desere
"""


class Student:
    """
    Represents a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Stud

        Args:
        attrs (list): Optional list of strings of attribute 

        Returns:
        dict: A dictionary containing key/values
        """
        if isinstance(attrs, list) and all(isinstance(item, str) for item in attrs):
            return {key: getattr(self, key) for key in attrs if hasattr(self, key)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the instance

        Args:
        json (dict): A dictionary with new attribute values.
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)

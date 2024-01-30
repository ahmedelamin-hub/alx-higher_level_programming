#!/usr/bin/python3
"""Defines class."""


class LockedClass:
    """
    A class that only allows creating an instance attribute named 'first_name'.
    """
    __slots__ = ['first_name']

#!/usr/bin/python

"""Defines a class LockedClass"""


class LockedClass:
    """
    Represents the class LockedClass.
    It prevents the user from dynamically creating
    new instance attributes
    """
    __slots__ = ["first_name"]

    def __init__(self, first_name=""):
        """Initialize the instance to be called."""
        self.first_name = first_name

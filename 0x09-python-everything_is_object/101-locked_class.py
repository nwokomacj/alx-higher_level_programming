#!/usr/bin/python

"""Defines a class LockedClass"""


class LockedClass:
    """
    Represents the class LockedClass.
    It prevents the user from dynamically creating
    new instance attributes
    """
    __slots__ = ["first_name"]
    """The only instance allowed th be called """

    def __init__(self, first_name=""):
        """Initialize the instance to be called."""
        self.firstname = first_name

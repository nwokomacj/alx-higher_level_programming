#!/usr/bin/python

"""Defines a class LockedClass"""


class LockedClass:
    """Represents the class LockedClass.
    It prevents the user from dynamically creating
    new instance attributes
    """
    ___slots___ = ["first_name"]
    """The only instance allowed th be called """
    def __init__(self, first_name=""):
        """Initialize the instance to be called.
        Args:
            None
        """
        self.firstname = first_name

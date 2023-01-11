#!/usr/bin/python3
"""Defines an inherited class-checking function"""


def inherits_from(obj, a_class):
    """checks if an object is an inherited instance of a class

    Args:
        obj (any): The object to chck
        a_class (type): The class to match the type of obj to
    Returns:
        if obj is an inherited of a_class - True
        otherwise - False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False

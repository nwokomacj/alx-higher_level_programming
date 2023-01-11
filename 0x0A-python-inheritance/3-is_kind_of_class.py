#!/usr/bin/python3
"""Defines a class and inherited class- cheching function"""


def is_kind_of_class(obj, a_class):
    """check if an objectis an instance or inherited instance of a class

    Args:
        obj (any): The object to check
        a_class (type): The class to match the type of obj tp.
    Returns:
        if obj is an instance or inherited instance of a_class - True
        otherwise - False
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False

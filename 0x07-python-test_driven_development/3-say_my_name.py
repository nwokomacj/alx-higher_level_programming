#!/usr/bin/python3
"""This module prints the fullname of the user"""

def say_my_name(first_name, last_name=""):
    """Prints the fullname
    Args:
        first_name: The first name of the fullname
        last_name: The last name of the fullname
    Returns: The first name and last name as the fullname
    Raise:
        TypeError: When firstname or last name is not a string
    """
    if not isinstance (first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    fullname = f"{first_name} {last_name}"
    print("My name is {}" .format(fullname))

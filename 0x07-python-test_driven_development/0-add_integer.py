#!/usr/bin/python3
"""This module adds two integres.
with a function ``add_integer(a, b=98)``"""


def add_integer(a, b=98):
    """Adds teo integers

    Args:
        a - first integer
        b - second integer

        Returns: the addition of a and b

         Float arguments are typecasted to ints
         before addition is performed.

        >>> add_integer = __import__('0-add_integer').add_integer
            >>> add_integer(2, 3)
                5

        Raises:
            A TypeError for exception of integer or float numbers
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)

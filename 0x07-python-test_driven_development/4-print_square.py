#!/usr/bin/python3
"""This module prints a square with the character '#'"""

def print_square(size):
    """Fuction that prints a square with # character
    Args:
        size: length of the square
    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
        TypeError: If size is a float
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float):
        raise TypeError("size must be an integer")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")

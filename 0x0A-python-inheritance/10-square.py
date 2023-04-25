#!/usr/bin/pyhton3
"""Defines a Rectangle subclass square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square
        """

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return(self.__size ** 2)

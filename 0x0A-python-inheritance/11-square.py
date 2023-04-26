#!/usr/bin/python3
"""Defines a Rectangle sublass square"""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represents a class square"""

    def __init__(self, size):
        """Initialize a new square

        Args:
            size(imt): The size of the new square
        """
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """Return area of the sqaure"""
        return (self.__size ** 2)

    def __str__(self):
        """print() and str() should return the square description"""
        string = "[Square] " + str(self.__size) + " "
        string += str(self.__size) + "/" + str(self.__size)
        return string

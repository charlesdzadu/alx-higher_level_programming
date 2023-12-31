#!/usr/bin/python3
"""Module to create a class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that inherits from Rectangle"""

    def __init__(self, size):
        """Instantiation with size"""
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Stringify square"""
        return "[Square] {}/{}".format(self.__size, self.__size)

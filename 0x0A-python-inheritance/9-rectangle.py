#!/usr/bin/python3
"""Module to create a class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle Class """

    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.__width = width
        self.__height = height

        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)

    def area(self):
        """Return area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Stringify rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

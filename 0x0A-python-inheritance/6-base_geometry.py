#!/usr/bin/python3
"""Module to create a class"""


class BaseGeometry:
    """Class with public instance method"""

    def area(self):
        """Exception for area() is not implemented"""
        raise Exception("area() is not implemented")

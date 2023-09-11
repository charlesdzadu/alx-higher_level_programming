#!/usr/bin/python3
"""Module to create a function"""


def is_same_class(obj, a_class):
    """Function that checks if an object is exactly
    an instance of the given class"""
    if type(obj) is a_class:
        return True
    else:
        return False

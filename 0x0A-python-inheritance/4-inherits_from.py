#!/usr/bin/python3
"""Module to create a function"""


def inherits_from(obj, a_class):
    """Function that check is object is instance of a class"""
    return isinstance(obj, a_class) and type(obj) is not a_class

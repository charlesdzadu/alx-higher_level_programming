#!/usr/bin/python3
"""Module to create a function"""


def add_attribute(obj, name, value):
    """Add two attributes to an object"""
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")

#!/usr/bin/python3
""" Module that adds two integers """


def add_integer(a, b=98):
    """ Function that adds two integers

    Args:
        a (int): first integer
        b (int): second integer
    Returns:
        int: sum of two integers

    Raises:
        TypeError: if a or b is not an integer or float
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

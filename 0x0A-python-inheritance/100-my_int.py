#!/usr/bin/python3
"""Module to create a class"""


class MyInt(int):
    """Supercharged int class"""

    def __eq__(self, other):
        """Override equality"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override inequality"""
        return super().__eq__(other)

#!/usr/bin/python3
"""Student to JSON module"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """Instantiation function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """To JSON function"""

        if (type(attrs) is list and
                all(type(ele) is str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

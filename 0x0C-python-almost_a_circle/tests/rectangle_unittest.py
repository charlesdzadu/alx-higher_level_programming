#!/usr/bin/python3
"""Module to test the function rectangle"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_rectangle_input(self):
        """Function to test the input the function rectangle"""

        self.assertRaises(TypeError, Rectangle, )

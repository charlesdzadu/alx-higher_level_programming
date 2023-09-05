#!/usr/bin/python3
"""Unittests for max_integer([..]). functions"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..]). funtions"""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 8]
        self.assertEqual(max_integer(ordered), 8)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 2, 7, 3]
        self.assertEqual(max_integer(unordered), 7)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [5, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 5)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [9]
        self.assertEqual(max_integer(one_element), 9)

    def test_floats(self):
        """Test a list of floats."""
        floats = [1.53, 6.33, -9.123, 23.8, 6.0]
        self.assertEqual(max_integer(floats), 23.8)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.53, 19.8, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 19.8)

    def test_string(self):
        """Test a string."""
        string = "Charles"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Charles", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)


if __name__ == '__main__':
    unittest.main()

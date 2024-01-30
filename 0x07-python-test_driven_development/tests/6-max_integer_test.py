#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Defines test cases for the max_integer function."""

    def test_max_at_end(self):
        """Test with the maximum integer at the end of the list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Test with the maximum integer at the beginning of the list."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Test with the maximum integer in the middle of the list."""
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_one_element(self):
        """Test a list with a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_negative_numbers(self):
        """Test a list with negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_none_input(self):
        """Test passing None as input."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_list_input(self):
        """Test passing non-list as input."""
        with self.assertRaises(TypeError):
            max_integer("string")

    def test_floats_and_integers(self):
        """Test a list with a mix of floats and integers."""
        self.assertEqual(max_integer([1.5, 2, 3.7, 4]), 4)

if __name__ == "__main__":
    unittest.main()

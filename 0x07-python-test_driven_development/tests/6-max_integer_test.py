#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from max_integer import max_integer # type: ignore

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function
    """

    def test_regular_list(self):
        """Test case for a regular list
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_reverse_sorted_list(self):
        """Test case for a reverse sorted list
        """
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_mixed_list(self):
        """Test case for a list with mixed numbers
        """
        self.assertEqual(max_integer([1, 3, -4, 2]), 3)

    def test_single_element_list(self):
        """Test case for a single element list
        """
        self.assertEqual(max_integer([4]), 4)

    def test_empty_list(self):
        """Test case for an empty list
        """
        self.assertEqual(max_integer([]), None)

    def test_float_list(self):
        """Test case for a list with floating point numbers
        """
        self.assertEqual(max_integer([1.5, 2.3, 3.7, 4.1]), 4.1)

    def test_duplicate_numbers_list(self):
        """Test case for a list with duplicate numbers
        """
        self.assertEqual(max_integer([1, 3, 4, 4, 2]), 4)

    def test_large_list(self):
        """Test case for a large list
        """
        self.assertEqual(max_integer(list(range(10000))), 9999)

if __name__ == '__main__':
    unittest.main()

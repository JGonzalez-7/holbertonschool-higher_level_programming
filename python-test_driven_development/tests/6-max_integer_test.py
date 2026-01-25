#!/usr/bin/python3
# Unittests for max_integer function (Holberton)

"""Unittest for max_integer([..])."""

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer."""

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_default_empty_list(self):
        self.assertIsNone(max_integer())

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_sorted_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unsorted_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_mixed_positive_negative(self):
        self.assertEqual(max_integer([-10, 0, 5, 3]), 5)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([9, 1, 2, 3]), 9)

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 9]), 9)

    def test_duplicate_max(self):
        self.assertEqual(max_integer([1, 9, 9, 2]), 9)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.7, 2.6]), 2.7)

    def test_mixed_int_float(self):
        self.assertEqual(max_integer([1, 2.5, 2, 2.4]), 2.5)

    def test_string_list(self):
        self.assertEqual(max_integer(["a", "b", "c"]), "c")

    def test_string_sentence(self):
        self.assertEqual(max_integer("Holberton"), "t")

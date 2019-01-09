#!/usr/bin/python3
""" Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_standard_int(self):
        self.assertEqual(max_integer([2, 4, 1, 3]), 4)

    def test_standard_float(self):
        self.assertEqual(max_integer([3.2, 5.7, 4.5]), 5.7)

    def test_infinity(self):
        self.assertEqual(max_integer([float('inf'), float('-inf')]),
                                     float('inf'))

    def test_type(self):
        with self.assertRaises(TypeError):
            max_integer(["Holberton", 7, 9, 15])

    def test_negatives(self):
        self.assertEqual(max_integer([-6, 3, -21, 1]), 3)

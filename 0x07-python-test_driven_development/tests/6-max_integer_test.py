#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
	"""Define unittests for max_integer([..])."""
	
    def ordered_test(self):
	"""Test an ordered list of integers"""
	ordered = [1, 2, 3, 4]
	self.assertEqual(max_integer(ordered), 4)

    def unordered_test(self):
	"""Test an unordered list of integers"""
	unordered = [2, 1, 4, 3]
	self.assertEqual(max_integer(unordered), 4)

    def empty_test(self):
	"""Test an empty list of integers"""
	empty = []
	self.assertEqual(max_integer(empty), None)

    def single_element_test(self):
        """Test an string list of integers"""
	single_element = [7]
	self.assertEqual(max_integer(single_element), 7)



if __name__ == '__main__':
    unittest.main()

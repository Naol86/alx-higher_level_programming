#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
	"""unit test cases"""
	def module_docstring(self):
		m = __import__('6-max_integer').__doc__
		self.assertTrue(len(m) > 1)
	
	def function_docstring(self):
		f = __import__("6-max_integer").max_integer.__doc__
		self.assertTrue(len(f) > 1)
	
	def empty_list(self):
		self.assertIsNone(max_integer([]))

if __name__ == "__main__":
	unittest.main()

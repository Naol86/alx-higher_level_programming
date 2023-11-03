#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """unit test cases"""
    def test_module_docstring(self):
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)

    def test_function_docstring(self):
        f = __import__("6-max_integer").max_integer.__doc__
        self.assertTrue(len(f) > 1)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_list(self):
        lis = [-12, -23, -24, -56]
        self.assertEqual(max_integer(lis), -12)

    def test_pos_neg(self):
        lis = [1, 2, 3, 4, -12, -45]
        self.assertEqual(max_integer(lis), 4)

    def test_invalid_input(self):
        lis = ["naol", 12, 34, "kasinet"]
        with self.assertRaises(TypeError):
            max_integer(lis)

    def test_None_list(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_integer(12)

if __name__ == "__main__":
    unittest.main()

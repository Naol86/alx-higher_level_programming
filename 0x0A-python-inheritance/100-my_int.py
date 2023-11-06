#!/usr/bin/python3
"""this int"""


class MyInt(int):
    """this is MyInt class"""
    def __eq__(self, other):
        return super().__eq__(other)
    def __ne__(self, other):
        return super().__ne__(other)

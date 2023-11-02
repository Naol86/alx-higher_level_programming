#!/usr/bin/python3
"""
This is the "0-add_integer" module.
The 0-add_integer module supplies one function, add_integer(a, b).
let's do it
"""


def add_integer(a, b=98):
    """
        this is add integer function to test doctest
    """
    if type(a) != float and type(a) != int:
        raise TypeError("a must be an integer")
    elif type(b) != float and type(b) != int:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b

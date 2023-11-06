#!/usr/bin/python3
"""lookup function"""


def lookup(obj):
    """
    Returns a list of all the attributes and methods of an object.

    Args:
        obj (any): The object for which we
        want to retrieve the attributes and methods.

    Returns:
        list: A list of attributes and methods of the input object.
    """
    return dir(obj)

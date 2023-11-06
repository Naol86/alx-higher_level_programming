#!/usr/bin/python3
""" this is checking class and obj
"""


def is_same_class(obj, a_class):
    """
    Check if an object is an instance of a specific class.

    Args:
        obj: The object to be checked.
        a_class: The class to compare the object against.

    Returns:
        True if obj is an instance of a_class, False otherwise.
    """
    if type(obj) == a_class:
        return True
    return False

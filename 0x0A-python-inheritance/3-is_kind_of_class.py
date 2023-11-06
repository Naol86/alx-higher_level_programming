#!/usr/bin/python3
"""is kind of class function"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of a given class.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        True if obj is an instance of a_class, False otherwise.
    """
    return isinstance(obj, a_class)

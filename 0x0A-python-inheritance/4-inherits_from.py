#!/usr/bin/python3
"""this is inherits from function"""


def inherits_from(obj, a_class):
    """
    Check if an object inherits from a specific class.

    Args:
        obj: The object to check if it inherits from a class.
        a_class: The class to check if the object inherits from.

    Returns:
        True if obj inherits from a_class, False otherwise.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
        return True
    return False

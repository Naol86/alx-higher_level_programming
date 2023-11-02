#!/usr/bin/python3
"""
this is a matrix test
"""


def matrix_divided(matrix, div):
    """matrix function"""
    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    size = None
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(i)
        if size is not None and size != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError(
                    "matrix must be a matrix (list of lists)\
                    of integers/floats")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(i / div, 2) for i in k] for k in matrix]

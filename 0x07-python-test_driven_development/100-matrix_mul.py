#!/usr/bin/python3
"""matrix multiplication
"""


def matrix_mul(m_a, m_b):
    """multiply matrix
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    size_a = None
    for i in m_a:
        if not isinstance(i, list):
            raise TypeError("m_a must be a list of lists")
        if len(i) == 0:
            raise ValueError("m_a can't be empty")
        if size_a is None:
            size_a = len(i)
        if size_a is not None and size_a != len(i):
            raise TypeError("each row of m_a must be of the same size")
        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError("m_a should contain only integers or floats")
    size_b = None
    for i in m_b:
        if not isinstance(i, list):
            raise TypeError("m_b must be a list of lists")
        if len(i) == 0:
            raise ValueError("m_b can't be empty")
        if size_b is None:
            size_b = len(i)
        if size_b is not None and size_b != len(i):
            raise TypeError("each row of m_b must be of the same size")
        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError("m_b should contain only integers or floats")
    if size_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    ans = []
    for i in range(len(m_a)):
        temp_ans = []
        for j in range(size_b):
            temp_sum = 0
            for k in range(len(m_b)):
                temp_sum += m_a[i][k] * m_b[k][j]
            temp_ans += [temp_sum]
        ans.append(temp_ans)
    return ans

#!/usr/bin/python3
"""
module contains 1 function:
    pascal_triangle
"""


def pascal_triangle(n):
    """ returns a pascal's triangle of size n

    Args:
        n: size of triangle
    """
    triangle = [[] for x in range(n)]
    if n <= 0:
        return []
    triangle[0] = [1]
    for i in range(n):
        if i == 0:
            triangle[i] = [1]
        if i == 1:
            triangle[i] = [1, 1]
        else:
            triangle[i].append(1)
            triangle[i].extend(
                triangle[i - 1][ii] + triangle[i - 1][ii + 1]
                for ii in range(i - 1))
            triangle[i].append(1)

    return triangle

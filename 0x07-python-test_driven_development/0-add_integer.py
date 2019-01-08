#!/usr/bin/python3
"""
This module, 0-add_integer contains one function:
add_integer(a, b)
"""
def add_integer(a, b=98):
    """ add_integer returns the sum of its two inputs

    Args:
        a: int
        b: int
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    a, b = int(a), int(b)
    return a + b

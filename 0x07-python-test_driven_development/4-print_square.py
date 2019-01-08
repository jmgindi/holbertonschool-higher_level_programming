#!/usr/bin/python3
"""
Module 4-print_square contains one function:
print_square(size)
"""
def print_square(size):
    """ print_square prints a square with side length size

    Args:
        size: must be an integer > 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for ii in range(size):
            print("#", end="")
        print()

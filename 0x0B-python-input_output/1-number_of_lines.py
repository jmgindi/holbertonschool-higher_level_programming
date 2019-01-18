#!/usr/bin/python3
"""
module contains 1 function:
    number_of_lines
"""

def number_of_lines(filename=""):
    """ number_of_lines returns the number of lines
    in a file

    Args:
        filename (obj:`str`): name of file
    """
    with open(filename) as f:
        return len(f.readlines())

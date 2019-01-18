#!/usr/bin/python3
"""
module contains 1 function:
    read_file
"""


def read_file(filename=""):
    """ reads a file

    Args:
        filename (obj:`str`): name of file
    """
    with open(filename) as f:
        print(f.read(), end="")

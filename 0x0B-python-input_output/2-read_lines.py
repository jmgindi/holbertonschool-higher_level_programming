#!/usr/bin/python3
"""
module contains 1 function:
    read_lines
"""


def read_lines(filename="", nb_lines=0):
    """ read_lines prints nb_lines lines of a file
    to stdout
    """
    with open(filename) as f:
        i = len(list(f))
        if nb_lines >= i or nb_lines <= 0:
            nb_lines = i
        f.seek(0, 0)
        for count in range(nb_lines):
            print(f.readline(), end="")

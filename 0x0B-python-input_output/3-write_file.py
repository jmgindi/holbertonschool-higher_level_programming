#!/usr/bin/python3
"""
module contains 1 function:
    write_file
"""


def write_file(filename="", text=""):
    """ write file writes text to file at filename.
    if the file does not exist, it creates a new one.
    if the file does exist, this function overwrites
    its contents

    Args:
        filename (obj:`str`): name of file
        text (obj:`str`): text to write
    """
    with open(filename, 'w') as f:
        return f.write(text)

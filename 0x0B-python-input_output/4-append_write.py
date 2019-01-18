#!/usr/bin/python3
"""
module contains 1 function:
    append_write
"""

def append_write(filename="", text=""):
    """ appends text to the end of the file at
    filename

    Args:
        filename (obj:`str`): name of file
        text (obj:`str`): text to append
    """
    with open(filename, 'a') as f:
        return f.write(text)

#!/usr/bin/python3
"""
Module 0-lookup contains 1 function:
lookup(obj)
"""
def lookup(obj):
    """ lookup returns the list of available attributes
    and methods of an object

    Args:
        obj (obj:`object`): any object
    """
    return (dir(obj))

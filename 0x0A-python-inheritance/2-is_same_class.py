#!/usr/bin/python3
"""
Module contains 1 function:
    is_same_class
"""
def is_same_class(obj, a_class):
    """ is_same_class returns True if obj is of class a_class
    or False if not

    Args:
        obj (obj:`object`): any object
        a_class (class): any class
    """
    if type(obj) is a_class:
        return True
    return False

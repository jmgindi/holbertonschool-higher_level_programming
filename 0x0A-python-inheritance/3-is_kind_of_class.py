#!/usr/bin/python3
"""
Module contains 1 function:
    is_kind_of_class
"""
def is_kind_of_class(obj, a_class):
    """ is_kind_of_class returns True if obj is of or a subclass
    of a_class, or False if not

    Args:
        obj (obj:`object`): any object
        a_class (class): any class
    """
    if issubclass(type(obj), a_class):
        return True
    return False

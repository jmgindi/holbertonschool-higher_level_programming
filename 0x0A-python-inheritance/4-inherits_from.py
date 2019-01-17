#!/usr/bin/python3
"""
Module contains 1 function:
    inherits_from
"""
def inherits_from(obj, a_class):
    """ inherits_from returns True if obj inherits from
    a_class, or False if not

    Args:
        obj (obj:`object`): any object
        a_class (class): any class
    """
    if not type(obj) is a_class and issubclass(type(obj), a_class):
        return True
    return False

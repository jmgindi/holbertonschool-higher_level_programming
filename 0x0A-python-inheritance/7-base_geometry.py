#!/usr/bin/python3
"""
Module contains 1 class:
    BaseGeometry
"""

class BaseGeometry():
    """ BaseGeometry is a class with one method:
        area - raises an Exception
        integer_validator - checks a value associated with name
    """
    def area(self):
        """ raises an exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ checks that the value associated with name is an int
        and greater than 0

        Args:
            name (obj:`str`): name of the value
            value (obj:`int`): value to check
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

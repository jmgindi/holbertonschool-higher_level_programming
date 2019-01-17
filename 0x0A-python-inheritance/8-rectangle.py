#!/usr/bin/python3
"""
Module contains 1 class:
    Rectangle (inherits from BaseGeometry)
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
class Rectangle(BaseGeometry):
    """ Rectangle defines a rectangle
    inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """ initializes a rectangle

        Args:
            width (obj:`int`): width of rectangle
            height (obj:`int`): height of rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

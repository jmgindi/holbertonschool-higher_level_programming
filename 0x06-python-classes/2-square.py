#!/usr/bin/python3
class Square:
    """ Square is a class that defines a square

    Attributes:
        size (int): size of square

    """

    def __init__(self, size=0):
        """ Init function for square class

        Args:
            size (int): for size attribute

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

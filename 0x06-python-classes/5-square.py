#!/usr/bin/python3
class Square:
    """Square is a class that defines a square

    Attributes:
        size (obj:`int`): size of square
        area (obj:`int`): area of square
    """

    def __init__(self, size=0):
        """Init function for square class

        Args:
            size (obj:`int`): for size attribute
        """
        self.__size = size

    def area(self):
        """Area calculates the area of a square
        """
        return self.__size ** 2

    @property
    def size(self):
        """returns size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """modifies size of a square

        Args:
            value (obj:`int`): value to modify size to
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """prints the square in hashes
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print('#' * self.__size)

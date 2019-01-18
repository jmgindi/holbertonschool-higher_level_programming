#!/usr/bin/python3
"""
module contains 1 class:
    Student
"""


class Student:
    """ student class

    Attributes:
        first_name (obj:`str`): first name
        last_name (obj:`str`): last name
        age (obj:`int`): age
    """
    def __init__(self, first_name, last_name, age):
        """ init method for Student

        Args:
            first_name: first name
            last_name: last name
            age: age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__

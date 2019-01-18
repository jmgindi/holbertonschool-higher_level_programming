#!/usr/bin/python3
import json
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

    def to_json(self, attrs=None):
        """ returns a json-serializable version of the object
        keys pulled from attrs, or the entire list is returned if
        attrs is not a list of strings

        Args:
            attrs: list of attributes
        """
        if type(attrs) is not list:
            return self.__dict__
        for element in attrs:
            if type(element) is not str:
                return self.__dict__
        return {key:value for (key,value) in self.__dict__.items() if key in attrs}

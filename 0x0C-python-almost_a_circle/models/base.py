#!/usr/bin/python3
import json
"""
module contains 1 class:
    Base
"""


class Base:
    """ Base keeps track of the number of objects

    Attributes:
        nb_objects (obj:`int`): private - number of objects
        id (obj:`int`): public - id of object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init method for Base class

        Args:
            id: object id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def nbreset(cls):
        """ resets __nb_objects for unittesting
        """
        cls.__nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """ turns a list of dictionaries into a json string

        Args:
            list_dictionaries
        """
        if list_dictionaries is None or []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ saves a list of objects of a class to a .json file
        """
        with open(cls.__name__ + ".json", "w") as f:
            f.write(cls.to_json_string([o.to_dictionary() for o in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """ loads a json string to a list of dictionaries
        """
        if json_string is None or "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ creates an object from a dictionary
        """
        o = cls(3, 3, 3)
        o.update(**dictionary)
        return o

    @classmethod
    def load_from_file(cls):
        """ loads instances of a class from a file
        file must be named <Class name>.json
        """
        try:
            with open(cls.__name__ + ".json", "r") as f:
                pass
        except FileNotFoundError:
            return []
        with open(cls.__name__ + ".json", "r") as f:
            ld = cls.from_json_string(f.read())
            return [cls.create(**d) for d in ld]

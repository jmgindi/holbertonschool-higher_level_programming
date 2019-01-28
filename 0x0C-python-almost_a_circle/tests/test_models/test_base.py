#!/usr/bin/python3
"""
unittest module for Base class
"""
import unittest
import json
from models.base import Base


class TestBase(unittest.TestCase):
    """ Base test case class
    """
    def setUp(self):
        """ setUp method resets nb_objects to 0
        """
        Base.nbreset()

    def test_Increment(self):
        """ tests that creating a new obj increments
        nb_objects
        """
        base = Base()
        self.assertEqual(base.id, base._Base__nb_objects)
        base2 = Base()
        self.assertEqual(base2.id, base2._Base__nb_objects)

    def test_IdIsString(self):
        """ tests id as string
        """
        basestr = Base("Blah")
        self.assertEqual(basestr.id, "Blah")

    def test_StringIdDNInb(self):
        """ tests incrementation with string id
        """
        base = Base("string")
        self.assertEqual(base._Base__nb_objects, 0)

    def test_ToJSON(self):
        """ tests to_json_string in base
        """
        b = Base()
        s = b.to_json_string([{'id': 1, 'test': 2}])
        self.assertEqual(json.loads(s), [{"id": 1, "test": 2}])

    def test_NotSerializable(self):
        """ gives to_json_string an object that
        isn`t serializable
        """
        b = Base()
        with self.assertRaises(TypeError):
            s = b.to_json_string([TypeError])

    def test_ArgCount(self):
        """ tests too many arguments to init
        """
        with self.assertRaises(TypeError):
            b = Base(7, 29, 31)

if __name__ == '__main__':
    unittest.main()

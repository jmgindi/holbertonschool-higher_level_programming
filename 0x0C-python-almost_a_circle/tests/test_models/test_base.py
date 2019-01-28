#!/usr/bin/python3
import unittest
import json
from models.base import Base
"""
unittest module for Base class
"""

class TestBase(unittest.TestCase):
    """ Base test case class
    """
    def setUp(self):
        Base.nbreset()

    def test_Increment(self):
        base = Base()
        self.assertEqual(base.id, base._Base__nb_objects)
        base2 = Base()
        self.assertEqual(base2.id, base2._Base__nb_objects)

    def test_IdIsString(self):
        basestr = Base("Blah")
        self.assertEqual(basestr.id, "Blah")

    def test_StringIdDNInb(self):
        base = Base("string")
        self.assertEqual(base._Base__nb_objects, 0)

    def test_ToJSON(self):
        b = Base()
        s = b.to_json_string([{'id': 1, 'test': 2}])
        self.assertEqual(json.loads(s), [{"id": 1, "test": 2}])

    def test_NotSerializable(self):
        b = Base()
        with self.assertRaises(TypeError):
            s = b.to_json_string([TypeError])

    def test_ArgCount(self):
        with self.assertRaises(TypeError):
            b = Base(7, 29, 31)

if __name__ == '__main__':
    unittest.main()

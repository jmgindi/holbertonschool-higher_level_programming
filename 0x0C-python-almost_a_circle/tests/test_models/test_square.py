#!/usr/bin/python3
import unittest
import json
import os
import sys
import io
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
"""
unittest module for square class
"""


class TestSquare(unittest.TestCase):
    """ TestCase class for square class
    """
    def setUp(self):
        """ setUp deletes Square.json if it exists
        as well as creating a new square and
        resetting nb_objects
        """
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass
        Base.nbreset()
        self.sqr = Square(5, 7, 1)

    def testBadInit(self):
        """ tests a zero argument init
        """
        with self.assertRaises(TypeError):
            r = Square()

    def testInitOneArg(self):
        """ tests init with one argument
        """
        r = Square(1)
        self.assertEqual(r.size, 1)

    def testTooManyArgs(self):
        """ tests init with too many arguments
        """
        with self.assertRaises(TypeError):
            r = Square(6, 6, 6, 6, 6, 6)

    def testSubclass(self):
        """ tests if Square is a subclass of Base
        """
        self.assertTrue(issubclass(type(self.sqr), Base))

    def testSubRect(self):
        """ tests if Square is a subclass of Rectangle
        """
        self.assertTrue(issubclass(type(self.sqr), Rectangle))

    def testSize(self):
        """ tests size
        """
        self.assertEqual(self.sqr.size, 5)

    def testSizeSetter(self):
        """ tests size setter
        """
        self.sqr.size = 3
        self.assertEqual(self.sqr.size, 3)

    def testX(self):
        """ tests x for square
        """
        self.assertEqual(self.sqr.x, 7)

    def testXSetter(self):
        """ tests x setter
        """
        self.sqr.x = 4
        self.assertEqual(self.sqr.x, 4)

    def testY(self):
        """ tests y
        """
        self.assertEqual(self.sqr.y, 1)

    def testYSetter(self):
        """ tests y setter
        """
        self.sqr.y = 5
        self.assertEqual(self.sqr.y, 5)

    def testID(self):
        """ tests id
        """
        self.assertEqual(self.sqr.id, 1)

    def testArea(self):
        """ tests area
        """
        self.assertEqual(self.sqr.area(), 25)

    def testStr(self):
        """ tests __str__
        """
        s = str(self.sqr)
        self.assertEqual(
            s, '[Square] (1) 7/1 - 5'
        )

    def testDisplayNoOffset(self):
        """ tests display with no offset
        """
        r = Square(2)
        with io.StringIO() as f, redirect_stdout(f):
            r.display()
            s = f.getvalue()
        self.assertEqual(s, "##\n##\n")

    def testDisplayWithX(self):
        """ tests display with x offset
        """
        r = Square(2, 1)
        with io.StringIO() as f, redirect_stdout(f):
            r.display()
            s = f.getvalue()
        self.assertEqual(s, " ##\n ##\n")

    def testDisplayWithY(self):
        """ tests display with y offset
        """
        r = Square(2, 0, 1)
        with io.StringIO() as f, redirect_stdout(f):
            r.display()
            s = f.getvalue()
        self.assertEqual(s, "\n##\n##\n")

    def testDisplayWithXandY(self):
        """ tests display with x and y offset
        """
        r = Square(2, 2, 2)
        with io.StringIO() as f, redirect_stdout(f):
            r.display()
            s = f.getvalue()
        self.assertEqual(s, "\n\n  ##\n  ##\n")

    def testUpdateArgs(self):
        """ tests update standard usage
        """
        self.sqr.update(1, 1, 1, 1)
        self.assertEqual(self.sqr.size, 1)
        self.assertEqual(self.sqr.x, 1)
        self.assertEqual(self.sqr.y, 1)
        self.assertEqual(self.sqr.id, 1)

    def testUpdateBadArgs(self):
        """ tests update with a bad argument
        """
        with self.assertRaises(TypeError):
            self.sqr.update(1, "hello world")

    def testUpdateNoArgs(self):
        """ tests update with no arguments
        """
        r = Square(5, 7, 1, 1)
        self.sqr.update()
        self.assertEqual(r.to_dictionary(), self.sqr.to_dictionary())

    @unittest.expectedFailure
    def testUpdateTooManyArgs(self):
        """ tests that update with too many arguments
        will not raise a TypeError
        """
        with self.assertRaises(TypeError):
            self.sqr.update(6, 6, 6, 6, 6, 6)

    def testUpdateKWargs(self):
        """ tests update with kwargs
        """
        d1 = self.sqr.to_dictionary()
        self.sqr.update(id="cat", size=1, x=1)
        d2 = self.sqr.to_dictionary()
        self.assertNotEqual(d1, d2)

    def testUpdateKWargsBadKey(self):
        """ tests update with a bad key
        """
        d1 = self.sqr.to_dictionary()
        self.sqr.update(boop=5)
        d2 = self.sqr.to_dictionary()
        self.assertEqual(d1, d2)

    def testUpdateMixedArgs(self):
        """ tests update with mixed arguments
        """
        self.sqr.update(3, id=4)
        self.assertEqual(self.sqr.id, 3)

    def testSqrToDict(self):
        """ tests square to dictionary
        """
        d = self.sqr.to_dictionary()
        self.assertEqual(
            d, {'size': 5, 'id': 1, 'x': 7, 'y': 1})

    def testSqrToJSONType(self):
        """ tests square to json's type
        """
        d = Square.to_json_string([self.sqr.to_dictionary()])
        self.assertIsInstance(d, str)

    def testSqrJSONHasAttrs(self):
        """ tests square to json retains attributes
        """
        d = Square.to_json_string([self.sqr.to_dictionary()])
        self.assertEqual(json.loads(d), [self.sqr.to_dictionary()])

    def testSqrEmptyToJSON(self):
        """ tests empty square to json
        """
        d = Square.to_json_string([])
        self.assertEqual(d, "[]")

    def testSqrNonetoJSON(self):
        """ tests an empty list to json string
        """
        d = Square.to_json_string(None)
        self.assertEqual(d, "[]")

    def testSaveSqrToFile(self):
        """ tests saving a square to a file
        """
        Square.save_to_file([self.sqr])
        with open("Square.json") as f:
            self.assertEqual(
                [self.sqr.to_dictionary()], json.load(f))

    def testSaveSqrsToFile(self):
        """ tests saving multiple squares to
        a file
        """
        r = Square(2, 2, 2)
        Square.save_to_file([self.sqr, r])
        with open("Square.json") as f:
            self.assertEqual(len(json.load(f)), 2)

    def testSaveNothingToFile(self):
        """ tests saving an empty list to a file
        """
        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertEqual(len(json.load(f)), 0)

    def testSaveBadFile(self):
        """ tests wrong type of argument to save_to_file
        """
        with self.assertRaises(AttributeError):
            Square.save_to_file("a string")

    def testFromJSON(self):
        """ tests loading a json string into a list
        of dicts
        """
        d = Square.from_json_string(
            '[{"id": 3, "size": 5, "x": 1, "y": 1}]'
        )
        self.assertEqual(d,
                         [{"id": 3, "size": 5, "x": 1, "y": 1}])

    def testFromJSONNonString(self):
        """ tests a bad type into from_json_string
        """
        with self.assertRaises(TypeError):
            d = Square.from_json_string(TypeError)

    def testFromJSONBadString(self):
        """ tests a non-json string to list of dicts
        """
        with self.assertRaises(ValueError):
            d = Square.from_json_string("bad string")

    def testCreateSquare(self):
        """ tests creation of a square
        """
        d = {"id": 1, "size": 5, "x": 2, "y": 2}
        r = Square.create(**d)
        self.assertEqual(d, r.to_dictionary())

    def testCreateBadSquare(self):
        """ tests creating a square with the wrong
        attributes
        """
        d = {"id": 1, "width": 2, "height": 2, "x": 2, "y": -1}
        with self.assertRaises(ValueError):
            r = Square.create(**d)

    def testCreateSqrEmptyDict(self):
        """ tests creating a square from an empty
        dictionary
        """
        d = {}
        r = Square.create(**d)
        self.assertEqual(r.id, 2)

    def testLoadSqrFromFile(self):
        """ tests loading a square from file
        """
        Square.save_to_file([self.sqr])
        r = Square.load_from_file()[0]
        self.assertEqual(
            self.sqr.to_dictionary(), r.to_dictionary())

    def testLoadNothingFromFile(self):
        """ tests loading an empty list from file
        """
        elist = []
        Square.save_to_file(elist)
        r = Square.load_from_file()
        self.assertEqual(elist, r)

    def testLoadSqrNoFile(self):
        """ tests loading a square if the file
        does not exist
        """
        r = Square.load_from_file()
        self.assertEqual(r, [])

    def testLoadBadSquare(self):
        """ tests a bad string loading from a file
        """
        with open("Square.json", "w") as f:
            f.write("Bad string")
        with self.assertRaises(ValueError):
            r = Square.load_from_file()

if __name__ == '__main__':
    unittest.main()

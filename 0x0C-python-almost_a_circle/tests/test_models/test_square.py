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
    """
    """
    def setUp(self):
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass
        Base.nbreset()
        self.sqr = Square(5, 7, 1)

    def testBadInit(self):
        with self.assertRaises(TypeError):
            r = Square()

    def testInitOneArg(self):
            r = Square(1)
            self.assertEqual(r.size, 1)

    def testTooManyArgs(self):
        with self.assertRaises(TypeError):
            r = Square(6, 6, 6, 6, 6, 6)

    def testSubclass(self):
        self.assertTrue(issubclass(type(self.sqr), Base))

    def testSize(self):
        self.assertEqual(self.sqr.size, 5)

    def testSizeSetter(self):
        self.sqr.size = 3
        self.assertEqual(self.sqr.size, 3)

    def testX(self):
        self.assertEqual(self.sqr.x, 7)

    def testXSetter(self):
        self.sqr.x = 4
        self.assertEqual(self.sqr.x, 4)

    def testY(self):
        self.assertEqual(self.sqr.y, 1)

    def testYSetter(self):
        self.sqr.y = 5
        self.assertEqual(self.sqr.y, 5)

    def testID(self):
        self.assertEqual(self.sqr.id, 1)

    def testArea(self):
        self.assertEqual(self.sqr.area(), 25)

    def testStr(self):
        s = str(self.sqr)
        self.assertEqual(
            s, '[Square] (1) 7/1 - 5'
        )

    def testDisplayNoOffset(self):
        r = Square(2)
        with io.StringIO() as f, redirect_stdout(f):
            r.display()
            s = f.getvalue()
        self.assertEqual(s, "##\n##\n")

    def testDisplayWithX(self):
        r = Square(2, 1)
        with io.StringIO() as f, redirect_stdout(f):
            r.display()
            s = f.getvalue()
        self.assertEqual(s, " ##\n ##\n")

    def testDisplayWithY(self):
        r = Square(2, 0, 1)
        with io.StringIO() as f, redirect_stdout(f):
            r.display()
            s = f.getvalue()
        self.assertEqual(s, "\n##\n##\n")

    def testDisplayWithXandY(self):
        r = Square(2, 2, 2)
        with io.StringIO() as f, redirect_stdout(f):
            r.display()
            s = f.getvalue()
        self.assertEqual(s, "\n\n  ##\n  ##\n")

    def testUpdateArgs(self):
        self.sqr.update(1, 1, 1, 1)
        self.assertEqual(self.sqr.size, 1)
        self.assertEqual(self.sqr.x, 1)
        self.assertEqual(self.sqr.y, 1)
        self.assertEqual(self.sqr.id, 1)

    def testUpdateBadArgs(self):
        with self.assertRaises(TypeError):
            self.sqr.update(1, "hello world")

    def testUpdateNoArgs(self):
        r = Square(5, 7, 1, 1)
        self.sqr.update()
        self.assertEqual(r.to_dictionary(), self.sqr.to_dictionary())

    @unittest.expectedFailure
    def testUpdateTooManyArgs(self):
        with self.assertRaises(TypeError):
            self.sqr.update(6, 6, 6, 6, 6, 6)

    def testUpdateKWargs(self):
        d1 = self.sqr.to_dictionary()
        self.sqr.update(id="cat", size=1, x=1)
        d2 = self.sqr.to_dictionary()
        self.assertNotEqual(d1, d2)

    def testUpdateKWargsBadKey(self):
        d1 = self.sqr.to_dictionary()
        self.sqr.update(boop=5)
        d2 = self.sqr.to_dictionary()
        self.assertEqual(d1, d2)

    def testUpdateMixedArgs(self):
        self.sqr.update(3, id=4)
        self.assertEqual(self.sqr.id, 3)

    def testSqrToDict(self):
        d = self.sqr.to_dictionary()
        self.assertEqual(
            d, {'size': 5, 'id': 1, 'x': 7, 'y': 1})

    def testSqrToJSONType(self):
        d = Square.to_json_string([self.sqr.to_dictionary()])
        self.assertIsInstance(d, str)

    def testSqrJSONHasAttrs(self):
        d = Square.to_json_string([self.sqr.to_dictionary()])
        self.assertEqual(json.loads(d), [self.sqr.to_dictionary()])

    def testSqrEmptyToJSON(self):
        d = Square.to_json_string([])
        self.assertEqual(d, "[]")

    def testSqrNonetoJSON(self):
        d = Square.to_json_string(None)
        self.assertEqual(d, "[]")

    def testSaveSqrToFile(self):
        Square.save_to_file([self.sqr])
        with open("Square.json") as f:
            self.assertEqual(
                [self.sqr.to_dictionary()], json.load(f))

    def testSaveSqrsToFile(self):
        r = Square(2, 2, 2)
        Square.save_to_file([self.sqr, r])
        with open("Square.json") as f:
            self.assertEqual(len(json.load(f)), 2)

    def testSaveNothingToFile(self):
        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertEqual(len(json.load(f)), 0)

    def testSaveBadFile(self):
        with self.assertRaises(AttributeError):
            Square.save_to_file("a string")

    def testFromJSON(self):
        d = Square.from_json_string(
            '[{"id": 3, "size": 5, "x": 1, "y": 1}]'
        )
        self.assertEqual(d,
                         [{"id": 3, "size": 5, "x": 1, "y": 1}]
        )

    def testFromJSONNonString(self):
        with self.assertRaises(TypeError):
            d = Square.from_json_string(TypeError)

    def testFromJSONBadString(self):
        with self.assertRaises(ValueError):
            d = Square.from_json_string("bad string")

    def testCreateSquare(self):
        d = {"id": 1, "size": 5, "x": 2, "y": 2}
        r = Square.create(**d)
        self.assertEqual(d, r.to_dictionary())

    def testCreateBadSquare(self):
        d = {"id": 1, "width": 2, "height": 2, "x": 2, "y": -1}
        with self.assertRaises(ValueError):
            r = Square.create(**d)

    def testCreateSqrEmptyDict(self):
        d = {}
        r = Square.create(**d)
        self.assertEqual(r.id, 2)

    def testLoadSqrFromFile(self):
        Square.save_to_file([self.sqr])
        r = Square.load_from_file()[0]
        self.assertEqual(
            self.sqr.to_dictionary(), r.to_dictionary())

    def testLoadNothingFromFile(self):
        elist = []
        Square.save_to_file(elist)
        r = Square.load_from_file()
        self.assertEqual(elist, r)

    def testLoadSqrNoFile(self):
        r = Square.load_from_file()
        self.assertEqual(r, [])

    def testLoadBadSquare(self):
        with open("Square.json", "w") as f:
            f.write("Bad string")
        with self.assertRaises(ValueError):
            r = Square.load_from_file()

if __name__ == '__main__':
    unittest.main()

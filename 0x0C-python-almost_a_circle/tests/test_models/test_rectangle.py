#!/usr/bin/python3
import unittest
import json
import os
import sys
import io
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
"""
unittest module for rectangle class
"""

class TestIntValidator(unittest.TestCase):
    """
    """
    def setUp(self):
        Base.nbreset()
        self.rect = Rectangle(2, 2, 2, 2)

    def testStdUsage(self):
        self.rect.width = 4
        self.assertEqual(self.rect.width, 4)

    def testNegID(self):
        self.rect.id = -5
        self.assertEqual(self.rect.id, -5)

    def testValidateType(self):
        with self.assertRaises(TypeError):
            self.rect.int_validator("x", 3.719)

    def testValidateTypeWidth(self):
        with self.assertRaises(TypeError):
            self.rect.width = "seven"

    def testValidateTypeHeight(self):
        with self.assertRaises(TypeError):
            self.rect.height = [1, 2, 3]

    def testValidateTypeX(self):
        with self.assertRaises(TypeError):
            self.rect.x = {'key': 'value'}

    def testValidateTypeY(self):
        with self.assertRaises(TypeError):
            self.rect.y = 'c'

    def testValidateNegWidth(self):
        with self.assertRaises(ValueError):
            self.rect.width = -50

    def testValidateNegHeight(self):
        with self.assertRaises(ValueError):
            self.rect.height = -5

    def testValidateZeroWidth(self):
        with self.assertRaises(ValueError):
            self.rect.width = 0

    def testValidateZeroHeight(self):
        with self.assertRaises(ValueError):
            self.rect.height = 0

    def testValidateZeroX(self):
        self.rect.x = 0
        self.assertEqual(self.rect.x, 0)

    def testValidateNegX(self):
        with self.assertRaises(ValueError):
            self.rect.x = -15

    def testValidateZeroY(self):
        self.rect.y = 0
        self.assertEqual(self.rect.y, 0)

    def testValidateNegY(self):
        with self.assertRaises(ValueError):
            self.rect.y = -1

class TestRectangle(unittest.TestCase):
    """
    """
    def setUp(self):
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        Base.nbreset()
        self.rect = Rectangle(5, 7, 1, 3)

    def testBadInit(self):
        with self.assertRaises(TypeError):
            r = Rectangle()

    def testBadInitOneArg(self):
        with self.assertRaises(TypeError):
            r = Rectangle(1)

    def testTooManyArgs(self):
        with self.assertRaises(TypeError):
            r = Rectangle(6, 6, 6, 6, 6, 6)

    def testSubclass(self):
        self.assertTrue(issubclass(type(self.rect), Base))

    def testWidth(self):
        self.assertEqual(self.rect.width, 5)

    def testWidthSetter(self):
        self.rect.width = 2
        self.assertEqual(self.rect.width, 2)

    def testHeight(self):
        self.assertEqual(self.rect.height, 7)

    def testHeightSetter(self):
        self.rect.height = 3
        self.assertEqual(self.rect.height, 3)

    def testX(self):
        self.assertEqual(self.rect.x, 1)

    def testXSetter(self):
        self.rect.x = 4
        self.assertEqual(self.rect.x, 4)

    def testY(self):
        self.assertEqual(self.rect.y, 3)

    def testYSetter(self):
        self.rect.y = 5
        self.assertEqual(self.rect.y, 5)

    def testID(self):
        self.assertEqual(self.rect.id, 1)

    def testArea(self):
        self.assertEqual(self.rect.area(), 35)

    def testStr(self):
        s = str(self.rect)
        self.assertEqual(
            s, '[Rectangle] (1) 1/3 - 5/7'
        )

    def testDisplayNoOffset(self):
        r = Rectangle(2, 2, 0, 0)
        with io.StringIO() as f, redirect_stdout(f):
            r.display()
            s = f.getvalue()
        self.assertEqual(s, "##\n##\n")

    def testDisplayWithX(self):
        r = Rectangle(2, 2, 1, 0)
        with io.StringIO() as f, redirect_stdout(f):
            r.display()
            s = f.getvalue()
        self.assertEqual(s, " ##\n ##\n")

    def testDisplayWithY(self):
        r = Rectangle(2, 2, 0, 1)
        with io.StringIO() as f, redirect_stdout(f):
            r.display()
            s = f.getvalue()
        self.assertEqual(s, "\n##\n##\n")

    def testDisplayWithXandY(self):
        r = Rectangle(2, 2, 2, 2)
        with io.StringIO() as f, redirect_stdout(f):
            r.display()
            s = f.getvalue()
        self.assertEqual(s, "\n\n  ##\n  ##\n")

    def testUpdateArgs(self):
        self.rect.update(1, 1, 1, 1, 1)
        self.assertEqual(self.rect.width, 1)
        self.assertEqual(self.rect.height, 1)
        self.assertEqual(self.rect.x, 1)
        self.assertEqual(self.rect.y, 1)
        self.assertEqual(self.rect.id, 1)

    def testUpdateBadArgs(self):
        with self.assertRaises(TypeError):
            self.rect.update(1, "hello world")

    def testUpdateNoArgs(self):
        r = Rectangle(5, 7, 1, 3, id=1)
        self.rect.update()
        self.assertEqual(r.to_dictionary(), self.rect.to_dictionary())

    @unittest.expectedFailure
    def testUpdateTooManyArgs(self):
        with self.assertRaises(TypeError):
            self.rect.update(6, 6, 6, 6, 6, 6)

    def testUpdateKWargs(self):
        d1 = self.rect.to_dictionary()
        self.rect.update(id="cat", width=1, x=1)
        d2 = self.rect.to_dictionary()
        self.assertNotEqual(d1, d2)

    def testUpdateKWargsBadKey(self):
        d1 = self.rect.to_dictionary()
        self.rect.update(boop=5)
        d2 = self.rect.to_dictionary()
        self.assertEqual(d1, d2)

    def testUpdateMixedArgs(self):
        self.rect.update(3, id=4)
        self.assertEqual(self.rect.id, 3)

    def testRectToDict(self):
        d = self.rect.to_dictionary()
        self.assertEqual(
            d, {'height': 7, 'id': 1, 'x': 1, 'width': 5, 'y': 3})

    def testRectToJSONType(self):
        d = Rectangle.to_json_string([self.rect.to_dictionary()])
        self.assertIsInstance(d, str)

    def testRectJSONHasAttrs(self):
        d = Rectangle.to_json_string([self.rect.to_dictionary()])
        self.assertEqual(json.loads(d), [self.rect.to_dictionary()])

    def testRectEmptyToJSON(self):
        d = Rectangle.to_json_string([])
        self.assertEqual(d, "[]")

    def testRectNonetoJSON(self):
        d = Rectangle.to_json_string(None)
        self.assertEqual(d, "[]")

    def testSaveRectToFile(self):
        Rectangle.save_to_file([self.rect])
        with open("Rectangle.json") as f:
            self.assertEqual(
                [self.rect.to_dictionary()], json.load(f))

    def testSaveRectsToFile(self):
        r = Rectangle(2, 2, 2, 2)
        Rectangle.save_to_file([self.rect, r])
        with open("Rectangle.json") as f:
            self.assertEqual(len(json.load(f)), 2)

    def testSaveNothingToFile(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json") as f:
            self.assertEqual(len(json.load(f)), 0)

    def testSaveBadFile(self):
        with self.assertRaises(AttributeError):
            Rectangle.save_to_file("a string")

    def testFromJSON(self):
        d = Rectangle.from_json_string(
            '[{"id": 3, "width": 5, "height": 5, "x": 1, "y": 1}]'
        )
        self.assertEqual(d,
                         [{"id": 3, "width": 5, "height": 5, "x": 1, "y": 1}]
        )

    def testFromJSONNonString(self):
        with self.assertRaises(TypeError):
            d = Rectangle.from_json_string(TypeError)

    def testFromJSONBadString(self):
        with self.assertRaises(ValueError):
            d = Rectangle.from_json_string("bad string")

    def testCreateRectangle(self):
        d = {"id": 1, "width": 2, "height": 2, "x": 2, "y": 2}
        r = Rectangle.create(**d)
        self.assertEqual(d, r.to_dictionary())

    def testCreateBadRectangle(self):
        d = {"id": 1, "width": 2, "height": 2, "x": 2, "y": -1}
        with self.assertRaises(ValueError):
            r = Rectangle.create(**d)

    def testCreateRectEmptyDict(self):
        d = {}
        r = Rectangle.create(**d)
        self.assertEqual(r.id, 2)

    def testLoadRectFromFile(self):
        Rectangle.save_to_file([self.rect])
        r = Rectangle.load_from_file()[0]
        self.assertEqual(
            self.rect.to_dictionary(), r.to_dictionary())

    def testLoadNothingFromFile(self):
        elist = []
        Rectangle.save_to_file(elist)
        r = Rectangle.load_from_file()
        self.assertEqual(elist, r)

    def testLoadRectNoFile(self):
        r = Rectangle.load_from_file()
        self.assertEqual(r, [])

    def testLoadBadRectangle(self):
        with open("Rectangle.json", "w") as f:
            f.write("Bad string")
        with self.assertRaises(ValueError):
            r = Rectangle.load_from_file()

if __name__ == '__main__':
    unittest.main()

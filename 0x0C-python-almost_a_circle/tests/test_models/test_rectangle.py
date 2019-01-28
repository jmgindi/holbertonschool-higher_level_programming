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
    """ TestCase for checking the int validator
    """
    def setUp(self):
        """ setUp function, resets nb_objects
        and creates a rectangle
        """
        Base.nbreset()
        self.rect = Rectangle(2, 2, 2, 2)

    def testStdUsage(self):
        """ standard usage
        """
        self.rect.width = 4
        self.assertEqual(self.rect.width, 4)

    def testNegID(self):
        """ negative as ID
        """
        self.rect.id = -5
        self.assertEqual(self.rect.id, -5)

    def testValidateType(self):
        """ tries to validate a float
        """
        with self.assertRaises(TypeError):
            self.rect.int_validator("x", 3.719)

    def testValidateTypeWidth(self):
        """ tries to validate a string as width
        """
        with self.assertRaises(TypeError):
            self.rect.width = "seven"

    def testValidateTypeHeight(self):
        """ tries to validate a list as height
        """
        with self.assertRaises(TypeError):
            self.rect.height = [1, 2, 3]

    def testValidateTypeX(self):
        """ tries to validate a dict as x
        """
        with self.assertRaises(TypeError):
            self.rect.x = {'key': 'value'}

    def testValidateTypeY(self):
        """ tries to validate a single character as y
        """
        with self.assertRaises(TypeError):
            self.rect.y = 'c'

    def testValidateNegWidth(self):
        """ tries a negative as width
        """
        with self.assertRaises(ValueError):
            self.rect.width = -50

    def testValidateNegHeight(self):
        """ negative height
        """
        with self.assertRaises(ValueError):
            self.rect.height = -5

    def testValidateZeroWidth(self):
        """ 0 as width
        """
        with self.assertRaises(ValueError):
            self.rect.width = 0

    def testValidateZeroHeight(self):
        """ 0 as height
        """
        with self.assertRaises(ValueError):
            self.rect.height = 0

    def testValidateZeroX(self):
        """ 0 as x
        """
        self.rect.x = 0
        self.assertEqual(self.rect.x, 0)

    def testValidateNegX(self):
        """ negative as x
        """
        with self.assertRaises(ValueError):
            self.rect.x = -15

    def testValidateZeroY(self):
        """ 0 as y
        """
        self.rect.y = 0
        self.assertEqual(self.rect.y, 0)

    def testValidateNegY(self):
        """ negative as y
        """
        with self.assertRaises(ValueError):
            self.rect.y = -1


class TestRectangle(unittest.TestCase):
    """ Rectangle TestCase for other functions
    """
    def setUp(self):
        """ setUp deletes Rectangle.json if it exists,
        resets nb_objects to 0, and creates a new rectangle
        """
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        Base.nbreset()
        self.rect = Rectangle(5, 7, 1, 3)

    def testBadInit(self):
        """ tests an init with no args
        """
        with self.assertRaises(TypeError):
            r = Rectangle()

    def testBadInitOneArg(self):
        """ only 1 arg
        """
        with self.assertRaises(TypeError):
            r = Rectangle(1)

    def testTooManyArgs(self):
        """ too many args to init
        """
        with self.assertRaises(TypeError):
            r = Rectangle(6, 6, 6, 6, 6, 6)

    def testSubclass(self):
        """ tests if Rectangle is a subclass of Base
        """
        self.assertTrue(issubclass(type(self.rect), Base))

    def testWidth(self):
        """ tests width
        """
        self.assertEqual(self.rect.width, 5)

    def testWidthSetter(self):
        """ tests the width setter
        """
        self.rect.width = 2
        self.assertEqual(self.rect.width, 2)

    def testHeight(self):
        """ tests height
        """
        self.assertEqual(self.rect.height, 7)

    def testHeightSetter(self):
        """ tests height setter
        """
        self.rect.height = 3
        self.assertEqual(self.rect.height, 3)

    def testX(self):
        """ tests x
        """
        self.assertEqual(self.rect.x, 1)

    def testXSetter(self):
        """ tests x setter
        """
        self.rect.x = 4
        self.assertEqual(self.rect.x, 4)

    def testY(self):
        """ tests y
        """
        self.assertEqual(self.rect.y, 3)

    def testYSetter(self):
        """ tests y setter
        """
        self.rect.y = 5
        self.assertEqual(self.rect.y, 5)

    def testID(self):
        """ tests id
        """
        self.assertEqual(self.rect.id, 1)

    def testArea(self):
        """ tests area
        """
        self.assertEqual(self.rect.area(), 35)

    def testStr(self):
        """ tests __str__
        """
        s = str(self.rect)
        self.assertEqual(
            s, '[Rectangle] (1) 1/3 - 5/7'
        )

    def testDisplayNoOffset(self):
        """ tests display with no offset
        """
        r = Rectangle(2, 2, 0, 0)
        with io.StringIO() as f, redirect_stdout(f):
            r.display()
            s = f.getvalue()
        self.assertEqual(s, "##\n##\n")

    def testDisplayWithX(self):
        """ tests display with only x offset
        """
        r = Rectangle(2, 2, 1, 0)
        with io.StringIO() as f, redirect_stdout(f):
            r.display()
            s = f.getvalue()
        self.assertEqual(s, " ##\n ##\n")

    def testDisplayWithY(self):
        """ tests display with only y offset
        """
        r = Rectangle(2, 2, 0, 1)
        with io.StringIO() as f, redirect_stdout(f):
            r.display()
            s = f.getvalue()
        self.assertEqual(s, "\n##\n##\n")

    def testDisplayWithXandY(self):
        """ tests display with both offsets
        """
        r = Rectangle(2, 2, 2, 2)
        with io.StringIO() as f, redirect_stdout(f):
            r.display()
            s = f.getvalue()
        self.assertEqual(s, "\n\n  ##\n  ##\n")

    def testUpdateArgs(self):
        """ updates args and tests them
        """
        self.rect.update(1, 1, 1, 1, 1)
        self.assertEqual(self.rect.width, 1)
        self.assertEqual(self.rect.height, 1)
        self.assertEqual(self.rect.x, 1)
        self.assertEqual(self.rect.y, 1)
        self.assertEqual(self.rect.id, 1)

    def testUpdateBadArgs(self):
        """ gives update a bad argument
        """
        with self.assertRaises(TypeError):
            self.rect.update(1, "hello world")

    def testUpdateNoArgs(self):
        """ tests update with no args
        """
        r = Rectangle(5, 7, 1, 3, id=1)
        self.rect.update()
        self.assertEqual(r.to_dictionary(), self.rect.to_dictionary())

    @unittest.expectedFailure
    def testUpdateTooManyArgs(self):
        """ tests that update with too many args does
        not raise a TypeError
        """
        with self.assertRaises(TypeError):
            self.rect.update(6, 6, 6, 6, 6, 6)

    def testUpdateKWargs(self):
        """ tests update with keyworded args
        """
        d1 = self.rect.to_dictionary()
        self.rect.update(id="cat", width=1, x=1)
        d2 = self.rect.to_dictionary()
        self.assertNotEqual(d1, d2)

    def testUpdateKWargsBadKey(self):
        """ tests giving a bad keyword to update
        """
        d1 = self.rect.to_dictionary()
        self.rect.update(boop=5)
        d2 = self.rect.to_dictionary()
        self.assertEqual(d1, d2)

    def testUpdateMixedArgs(self):
        """ tests that args supersedes kwargs
        """
        self.rect.update(3, id=4)
        self.assertEqual(self.rect.id, 3)

    def testRectToDict(self):
        """ tests to_dictionary
        """
        d = self.rect.to_dictionary()
        self.assertEqual(
            d, {'height': 7, 'id': 1, 'x': 1, 'width': 5, 'y': 3})

    def testRectToJSONType(self):
        """ tests the type of to_json_string's return
        """
        d = Rectangle.to_json_string([self.rect.to_dictionary()])
        self.assertIsInstance(d, str)

    def testRectJSONHasAttrs(self):
        """ tests that to_json_string works properly
        """
        d = Rectangle.to_json_string([self.rect.to_dictionary()])
        self.assertEqual(json.loads(d), [self.rect.to_dictionary()])

    def testRectEmptyToJSON(self):
        """ tests an empty list into to_json_string
        """
        d = Rectangle.to_json_string([])
        self.assertEqual(d, "[]")

    def testRectNonetoJSON(self):
        """ tests None into to_json_string
        """
        d = Rectangle.to_json_string(None)
        self.assertEqual(d, "[]")

    def testSaveRectToFile(self):
        """ tests saving a rectangle to a file
        """
        Rectangle.save_to_file([self.rect])
        with open("Rectangle.json") as f:
            self.assertEqual(
                [self.rect.to_dictionary()], json.load(f))

    def testSaveRectsToFile(self):
        """ tests saving multiple rectangles to a file
        """
        r = Rectangle(2, 2, 2, 2)
        Rectangle.save_to_file([self.rect, r])
        with open("Rectangle.json") as f:
            self.assertEqual(len(json.load(f)), 2)

    def testSaveNothingToFile(self):
        """ tests saving an empty list to a file
        """
        Rectangle.save_to_file([])
        with open("Rectangle.json") as f:
            self.assertEqual(len(json.load(f)), 0)

    def testSaveBadFile(self):
        """ tests that saving a non-serializable object
        will raise an error
        """
        with self.assertRaises(AttributeError):
            Rectangle.save_to_file("a string")

    def testFromJSON(self):
        """ tests from_json_string
        """
        d = Rectangle.from_json_string(
            '[{"id": 3, "width": 5, "height": 5, "x": 1, "y": 1}]'
        )
        self.assertEqual(d,
                         [{"id": 3, "width": 5, "height": 5, "x": 1, "y": 1}])

    def testFromJSONNonString(self):
        """ tests from_json_string with a bad
        input
        """
        with self.assertRaises(TypeError):
            d = Rectangle.from_json_string(TypeError)

    def testFromJSONBadString(self):
        """ tests from_json_string with a non-serializable
        """
        with self.assertRaises(ValueError):
            d = Rectangle.from_json_string("bad string")

    def testCreateRectangle(self):
        """ tests create
        """
        d = {"id": 1, "width": 2, "height": 2, "x": 2, "y": 2}
        r = Rectangle.create(**d)
        self.assertEqual(d, r.to_dictionary())

    def testCreateBadRectangle(self):
        """ tests create with a bad dict
        """
        d = {"id": 1, "width": 2, "height": 2, "x": 2, "y": -1}
        with self.assertRaises(ValueError):
            r = Rectangle.create(**d)

    def testCreateRectEmptyDict(self):
        """ tests create on an empty dict
        """
        d = {}
        r = Rectangle.create(**d)
        self.assertEqual(r.id, 2)

    def testLoadRectFromFile(self):
        """ tests load_from_file
        """
        Rectangle.save_to_file([self.rect])
        r = Rectangle.load_from_file()[0]
        self.assertEqual(
            self.rect.to_dictionary(), r.to_dictionary())

    def testLoadNothingFromFile(self):
        """ tests loading an empty list from a file
        """
        elist = []
        Rectangle.save_to_file(elist)
        r = Rectangle.load_from_file()
        self.assertEqual(elist, r)

    def testLoadRectNoFile(self):
        """ tests loading from a non-existent file
        """
        r = Rectangle.load_from_file()
        self.assertEqual(r, [])

    def testLoadBadRectangle(self):
        """ tests loading a non-json object as a rectangle
        """
        with open("Rectangle.json", "w") as f:
            f.write("Bad string")
        with self.assertRaises(ValueError):
            r = Rectangle.load_from_file()

if __name__ == '__main__':
    unittest.main()

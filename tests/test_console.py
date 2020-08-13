#!/usr/bin/python3
""" Test case for console """
import unittest
from unittest import TestCase
from unittest.mock import patch
import pep8
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os
import sys
import console
from console import HBNBCommand
from io import StringIO


class TestPep8B(unittest.TestCase):
    """ Test pep8 style validation """
    def test_pep8(self):
        """ test base and test_base for pep8 conformance """
        style = pep8.StyleGuide(quiet=True)
        file1 = 'console.py'
        file2 = 'tests/test_console.py'
        result = style.check_files([file1, file2])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warning).")


class TestDocsB(unittest.TestCase):
    """ check for documentation """
    def test_module_doc(self):
        """ check for module documentation """
        self.assertTrue(len(console.__doc__) > 0)

    def test_class_doc(self):
        """ check for documentation """
        self.assertTrue(len(HBNBCommand.__doc__) > 0)

    def test_method_docs(self):
        """ check for method documentation """
        for func in dir(HBNBCommand):
            self.assertTrue(len(func.__doc__) > 0)


class ConsoleTestClass(unittest.TestCase):
    """ Class to test case of input in console """

    def setUp(self):
        """ create instance global """
        self.instan = HBNBCommand()

    def tearDown(self):
        """ Clean all test case """
        pass

    def test_create(self):
        """ Test Case to create a object from a class """

        with patch('sys.stdout', new=StringIO()) as test_cmd:
            self.instan.onecmd('create')
            self.assertEqual('** class name missing **\n', test_cmd.getvalue())

        with patch('sys.stdout', new=StringIO()) as test_cmd:
            self.instan.onecmd('create Class')
            self.assertEqual('** class doesn\'t exist **\n',
                             test_cmd.getvalue())

        with patch('sys.stdout', new=StringIO()) as test_cmd:
            self.instan.onecmd('create User')
            self.assertTrue(len(test_cmd.getvalue()) > 0)

        with patch('sys.stdout', new=StringIO()) as test_cmd:
            self.instan.onecmd('all State')
            self.assertTrue(len(test_cmd.getvalue()) > 0)


if __name__ == '__main__':
    unittest.main()

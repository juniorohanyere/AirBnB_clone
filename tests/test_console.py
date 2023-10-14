#!/usr/bin/env python3
"""Unittest console module.

Test cases for console class and methods documentation and instances.
"""

import unittest
import pep8
import sys
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.base_model import BaseModel
from models.__init__ import storage


class TestBase(unittest.TestCase):
    """TextMaxInteger(unittest.TesCase)
    Args:
        unittest (Test): analysis of data
    """

    def test_pep8_compliance(self):
        """... test code style errors and warnings
        """

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_compliance_test(self):
        """... test code style errors and warnings
        """

        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_HBNBCommand_exist(self):
        """... Check if methods exists
        """

        # self.assertTrue(hasattr(HBNBCommand, "do_prompt"))
        self.assertTrue(hasattr(HBNBCommand, "do_quit"))
        self.assertTrue(hasattr(HBNBCommand, "do_EOF"))
        # self.assertTrue(hasattr(HBNBCommand, "find_class"))
        self.assertTrue(hasattr(HBNBCommand, "do_create"))
        self.assertTrue(hasattr(HBNBCommand, "do_show"))
        self.assertTrue(hasattr(HBNBCommand, "do_destroy"))
        self.assertTrue(hasattr(HBNBCommand, "do_update"))
        self.assertTrue(hasattr(HBNBCommand, "do_all"))
        self.assertTrue(hasattr(HBNBCommand, "do_count"))
        self.assertTrue(hasattr(HBNBCommand, "emptyline"))
        self.assertTrue(hasattr(HBNBCommand, "default"))
        self.assertTrue(hasattr(HBNBCommand, "precmd"))
        self.assertTrue(hasattr(HBNBCommand, "onecmd"))
        self.assertTrue(hasattr(HBNBCommand, "HBNBCommand_error_handler"))

    def test_HBNBCommand_doc(self):
        """... Check the documentation
        """

        self.assertIsNotNone(HBNBCommand.__doc__)
        # self.assertIsNotNone(HBNBCommand.do_prompt.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        # self.assertIsNotNone(HBNBCommand.find_class.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_count.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.default.__doc__)
        self.assertIsNotNone(HBNBCommand.precmd.__doc__)
        self.assertIsNotNone(HBNBCommand.onecmd.__doc__)
        self.assertIsNotNone(HBNBCommand.HBNBCommand_error_handler.__doc__)

    def test_HBNBCommand_1(self):
        """... test 1
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")

    def test_HBNBCommand_2(self):
        """... test 2
        """

        update = "update BaseModel fce4d085-ebc6-4472-ae0e-82e2a0db7e5a" + \
            "first_name \"Betty\""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 1234-1234-1234")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 1234-1234-1234")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(update)

    def test_HBNBCommand_3(self):
        """... test 3
        """

        update = "update User fce4d085-ebc6-4472-ae0e-82e2a0db7e5a" + \
            "first_name \"Betty\""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show Place 1234-1234-1234")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy Review 1234-1234-1234")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all State")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(update)

    def test_HBNBCommand_4(self):
        """... test 4
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.all()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.all()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.all()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.all()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Reivew.all()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")

    def test_HBNBCommand_5(self):
        """... test 5
        """

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.count()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.count()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.count()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.count()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Reivew.count()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")

    def test_HBNBCommand_6(self):
        """... test 6
        """

        User = "User.show(\"246c227a-d5c1-403d-9bc7-6a47bb9f0f68\")"
        Place = "Place.show(\"fce4d085-ebc6-4472-ae0e-82e2a0db7e5a\")"
        State = "State.show(\"5fb793e6-9c5a-4063-9c60-2f3f5a061d95\")"
        City = "City.show(\"323f3340-1246-48e5-a47d-64d0e74349be\")"
        Amenity = "Amenity.show(\"7a6d7852-9368-4138-889b-8b3086a51885\")"
        Reivew = "Reivew.show(\"7aeaff10-96dd-4754-b429-8e0f7f645e47\")"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(Place)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(State)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(City)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(Amenity)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(Reivew)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(User)

    def test_HBNBCommand_7(self):
        """... test 7
        """

        User = "User.destroy(\"246c227a-d5c1-403d-9bc7-6a47bb9f0f68\")"
        Place = "Place.destroy(\"fce4d085-ebc6-4472-ae0e-82e2a0db7e5a\")"
        State = "State.destroy(\"5fb793e6-9c5a-4063-9c60-2f3f5a061d95\")"
        City = "City.destroy(\"323f3340-1246-48e5-a47d-64d0e74349be\")"
        Amenity = "Amenity.destroy(\"7a6d7852-9368-4138-889b-8b3086a51885\")"
        Reivew = "Reivew.destroy(\"7aeaff10-96dd-4754-b429-8e0f7f645e47\")"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(Place)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(State)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(City)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(Amenity)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(Reivew)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(User)

    def test_HBNBCommand_8(self):
        """... test 8
        """

        User = "User.update(\"38f22813-2753-4d42-b37c-57a17f1e4f88\", " + \
            "\"first_name\", \"Erika\")"
        Place = "Place.update(\"246c227a-d5c1-403d-9bc7-6a47bb9f0f68\", " + \
            "\"first_name\", \"Osorio\")"
        State = "State.update(\"5fb793e6-9c5a-4063-9c60-2f3f5a061d95\", " + \
            "\"first_name\", \"Edison\")"
        City = "City.update(\"7a6d7852-9368-4138-889b-8b3086a51885\", " + \
            "\"first_name\", \"Esteban\")"
        Amenity = "Amenity.update(\"fce4d085-ebc6-4472-ae0e-82e2a0db\", " + \
            "\"first_name\", \"Isaza\")"
        Reivew = "Reivew .update(\"7aeaff10-96dd-4754-b429-8e0f7f645e47\"," + \
            "\"first_name\", \"John\")"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(Place)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(State)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(City)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(Amenity)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(Reivew)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(User)

    def test_HBNBCommand_9(self):
        """... test 9
        """

        User = "User.update(\"38f22813-2753-4d42-b37c-57a17f1e4f88\", " + \
            "{'first_name': \"Erika\", \"age\": 9})"
        Place = "Place.update(\"246c227a-d5c1-403d-9bc7-6a47bb9f0f68\", " + \
            "{'first_name': \"Osorio\", \"age\": 29})"
        State = "State.update(\"5fb793e6-9c5a-4063-9c60-2f3f5a061d95\", " + \
            "{'first_name': \"Esteban\", \"age\": 59})"
        City = "City.update(\"7a6d7852-9368-4138-889b-8b3086a51885\", " + \
            "{'first_name': \"Lopez\", \"age\": 86})"
        Amenity = "Amenity.update(\"fce4d085-ebc6-4472-ae0e-82e2a0db\", " + \
            "{'first_name': \"Castañeda\", \"age\": 34})"
        Reivew = "Reivew .update(\"7aeaff10-96dd-4754-b429-8e0f7f645e47\"," + \
            "{'first_name': \"Andres\", \"age\": 80})"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(Place)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(State)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(City)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(Amenity)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(Reivew)
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(User)

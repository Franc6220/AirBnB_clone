#!/usr/bin/python3
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json

class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        """Prepare the environment for each test."""
        self.console = HBNBCommand()

    def tearDown(self):
        """Clean up the environment after each test."""
        storage.all().clear()
        storage.save()

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        """Test the create command."""
        self.console.onecmd("create BaseModel")
        output = mock_stdout.getvalue().strip()
        self.assertTrue(len(output) == 36)  # ID length is 36 characters

        self.console.onecmd("create User")
        output = mock_stdout.getvalue().strip().split('\n')[-1]
        self.assertTrue(len(output) == 36)

        self.console.onecmd("create InvalidClass")
        output = mock_stdout.getvalue().strip().split('\n')[-1]
        self.assertEqual(output, "** class doesn't exist **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        """Test the show command."""
        base_model = BaseModel()
        base_model.save()
        self.console.onecmd(f"show BaseModel {base_model.id}")
        output = mock_stdout.getvalue().strip()
        self.assertIn(base_model.id, output)

        self.console.onecmd("show BaseModel invalid_id")
        output = mock_stdout.getvalue().strip().split('\n')[-1]
        self.assertEqual(output, "** no instance found **")

        self.console.onecmd("show InvalidClass")
        output = mock_stdout.getvalue().strip().split('\n')[-1]
        self.assertEqual(output, "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy(self, mock_stdout):
        """Test the destroy command."""
        base_model = BaseModel()
        base_model.save()
        self.console.onecmd(f"destroy BaseModel {base_model.id}")
        self.assertNotIn(base_model.id, storage.all())

        self.console.onecmd("destroy BaseModel invalid_id")
        output = mock_stdout.getvalue().strip().split('\n')[-1]
        self.assertEqual(output, "** no instance found **")

        self.console.onecmd("destroy InvalidClass")
        output = mock_stdout.getvalue().strip().split('\n')[-1]
        self.assertEqual(output, "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_all(self, mock_stdout):
        """Test the all command."""
        base_model = BaseModel()
        base_model.save()
        self.console.onecmd("all")
        output = mock_stdout.getvalue().strip()
        self.assertIn(base_model.id, output)

        self.console.onecmd("all BaseModel")
        output = mock_stdout.getvalue().strip()
        self.assertIn(base_model.id, output)

        self.console.onecmd("all InvalidClass")
        output = mock_stdout.getvalue().strip().split('\n')[-1]
        self.assertEqual(output, "** class doesn't exist **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update(self, mock_stdout):
        """Test the update command."""
        base_model = BaseModel()
        base_model.save()
        self.console.onecmd(f"update BaseModel {base_model.id} name 'test'")
        self.assertEqual(base_model.name, 'test')

        self.console.onecmd("update BaseModel invalid_id name 'test'")
        output = mock_stdout.getvalue().strip().split('\n')[-1]
        self.assertEqual(output, "** no instance found **")

        self.console.onecmd("update InvalidClass")
        output = mock_stdout.getvalue().strip().split('\n')[-1]
        self.assertEqual(output, "** class name missing **")

    @patch('sys.stdout', new_callable=StringIO)
    def test_count(self, mock_stdout):
        """Test the count command."""
        self.console.onecmd("User.create()")
        self.console.onecmd("User.create()")
        self.console.onecmd("User.count()")
        output = mock_stdout.getvalue().strip().split('\n')[-1]
        self.assertEqual(output, '2')

    @patch('sys.stdout', new_callable=StringIO)
    def test_class_show(self, mock_stdout):
        """Test the <class name>.show(<id>) command."""
        base_model = BaseModel()
        base_model.save()
        self.console.onecmd(f"BaseModel.show({base_model.id})")
        output = mock_stdout.getvalue().strip()
        self.assertIn(base_model.id, output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_class_destroy(self, mock_stdout):
        """Test the <class name>.destroy(<id>) command."""
        base_model = BaseModel()
        base_model.save()
        self.console.onecmd(f"BaseModel.destroy({base_model.id})")
        self.assertNotIn(base_model.id, storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_class_update_with_dict(self, mock_stdout):
        """Test the <class name>.update(<id>, <dictionary representation>) command."""
        base_model = BaseModel()
        base_model.save()
        self.console.onecmd(f"BaseModel.update({base_model.id}, {{'name': 'test', 'number': 89}})")
        self.assertEqual(base_model.name, 'test')
        self.assertEqual(base_model.number, 89)

if __name__ == '__main__':
    unittest.main()


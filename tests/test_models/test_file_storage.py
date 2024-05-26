#!/usr/bin/python3
# tests/test_models/test_file_storage.py
import unittest
import json
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.file_path = FileStorage._FileStorage__file_path
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        bm = BaseModel()
        self.storage.new(bm)
        key = f"BaseModel.{bm.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        bm = BaseModel()
        self.storage.new(bm)
        self.storage.save()
        with open(self.file_path, 'r') as file:
            obj_dict = json.load(file)
        key = f"BaseModel.{bm.id}"
        self.assertIn(key, obj_dict)

    def test_reload(self):
        bm = BaseModel()
        self.storage.new(bm)
        self.storage.save()
        FileStorage._FileStorage__objects = {}
        self.storage.reload()
        key = f"BaseModel.{bm.id}"
        self.assertIn(key, self.storage.all())

if __name__ == '__main__':
    unittest.main()


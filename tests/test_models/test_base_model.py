#!/usr/bin/python3
# tests/test_models/test_base_model.py
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_instantiation(self):
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)

if __name__ == "__main__":
    unittest.main()

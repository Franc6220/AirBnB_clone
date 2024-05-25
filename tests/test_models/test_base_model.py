# tests/test_base_model.py

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid

class TestBaseModel(unittest.TestCase):
    def test_id_is_unique(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)
        self.assertIsInstance(bm2.id, str)

    def test_created_at_initialization(self):
        bm = BaseModel()
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)
        self.assertEqual(bm.created_at, bm.updated_at)

    def test_str_method(self):
        bm = BaseModel()
        expected_str = f"[BaseModel] ({bm.id}) {bm.__dict__}"
        self.assertEqual(str(bm), expected_str)

    def test_save_method(self):
        bm = BaseModel()
        old_updated_at = bm.updated_at
        bm.save()
        self.assertNotEqual(bm.updated_at, old_updated_at)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_to_dict_method(self):
        bm = BaseModel()
        dict_repr = bm.to_dict()
        self.assertEqual(dict_repr['id'], bm.id)
        self.assertEqual(dict_repr['__class__'], 'BaseModel')
        self.assertEqual(dict_repr['created_at'], bm.created_at.isoformat())
        self.assertEqual(dict_repr['updated_at'], bm.updated_at.isoformat())
        self.assertIsInstance(dict_repr['created_at'], str)
        self.assertIsInstance(dict_repr['updated_at'], str)

if __name__ == '__main__':
    unittest.main()


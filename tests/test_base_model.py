#!/usr/bin/python3
"""Tests for the BaseModel class."""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test BaseModel functionality."""

    def test_instance_attributes(self):
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_unique_ids(self):
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_str(self):
        obj = BaseModel()
        self.assertIn("BaseModel", str(obj))
        self.assertIn(obj.id, str(obj))

    def test_to_dict(self):
        obj = BaseModel()
        data = obj.to_dict()
        self.assertEqual(data["__class__"], "BaseModel")
        self.assertEqual(data["id"], obj.id)
        self.assertIsInstance(data["created_at"], str)
        self.assertIsInstance(data["updated_at"], str)

    def test_kwargs_reconstruction(self):
        obj = BaseModel()
        data = obj.to_dict()
        new_obj = BaseModel(**data)
        self.assertEqual(new_obj.id, obj.id)
        self.assertIsInstance(new_obj.created_at, datetime)
        self.assertIsInstance(new_obj.updated_at, datetime)

    def test_save(self):
        obj = BaseModel()
        previous = obj.updated_at
        obj.save()
        self.assertGreaterEqual(obj.updated_at, previous)


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/python3
"""Tests for the project model classes."""
import unittest
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestModels(unittest.TestCase):
    """Test model attributes."""

    def test_user(self):
        obj = User()
        self.assertEqual(obj.email, "")
        self.assertEqual(obj.password, "")
        self.assertEqual(obj.first_name, "")
        self.assertEqual(obj.last_name, "")

    def test_state(self):
        obj = State()
        self.assertEqual(obj.name, "")

    def test_city(self):
        obj = City()
        self.assertEqual(obj.state_id, "")
        self.assertEqual(obj.name, "")

    def test_amenity(self):
        obj = Amenity()
        self.assertEqual(obj.name, "")

    def test_place(self):
        obj = Place()
        self.assertEqual(obj.city_id, "")
        self.assertEqual(obj.user_id, "")
        self.assertEqual(obj.name, "")
        self.assertEqual(obj.description, "")
        self.assertEqual(obj.number_rooms, 0)
        self.assertEqual(obj.number_bathrooms, 0)
        self.assertEqual(obj.max_guest, 0)
        self.assertEqual(obj.price_by_night, 0)
        self.assertEqual(obj.latitude, 0.0)
        self.assertEqual(obj.longitude, 0.0)
        self.assertEqual(obj.amenity_ids, [])

    def test_review(self):
        obj = Review()
        self.assertEqual(obj.place_id, "")
        self.assertEqual(obj.user_id, "")
        self.assertEqual(obj.text, "")


if __name__ == "__main__":
    unittest.main()

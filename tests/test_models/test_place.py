#!/usr/bin/python3
import unittest
from models.place import Place

class TestPlace(unittest.TestCase):

    def test_default_values(self):
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        # ... agregar más aserciones para los demás atributos

if __name__ == '__main__':
    unittest.main()

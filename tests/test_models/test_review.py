#!/usr/bin/python3
import unittest
from models.review import Review

class TestReview(unittest.TestCase):

    def test_default_values(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

if __name__ == '__main__':
    unittest.main()

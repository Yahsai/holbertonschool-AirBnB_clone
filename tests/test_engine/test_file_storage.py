#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os

class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """
        Set up for the test: instantiate FileStorage and BaseModel.
        """
        self.storage = FileStorage()
        self.model = BaseModel()

    def tearDown(self):
        """
        Clean up after the test: delete the JSON file if it exists.
        """
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all_method(self):
        """
        Test the all method of FileStorage.
        """
        all_objects = self.storage.all()
        self.assertIsInstance(all_objects, dict)

    def test_new_method(self):
        """
        Test the new method of FileStorage.
        """
        obj_id = self.model.id
        self.storage.new(self.model)
        all_objects = self.storage.all()
        self.assertIn(f"{self.model.__class__.__name__}.{obj_id}", all_objects)

    def test_save_method(self):
        """
        Test the save method of FileStorage.
        """
        obj_id = self.model.id
        self.storage.new(self.model)
        self.storage.save()
        file_path = FileStorage._FileStorage__file_path
        self.assertTrue(os.path.exists(file_path))

    def test_reload_method(self):
        """
        Test the reload method of FileStorage.
        """
        obj_id = self.model.id
        self.storage.new(self.model)
        self.storage.save()
        self.storage.reload()
        all_objects = self.storage.all()
        self.assertIn(f"{self.model.__class__.__name__}.{obj_id}", all_objects)

if __name__ == '__main__':
    unittest.main()

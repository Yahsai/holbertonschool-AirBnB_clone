#!/usr/bin/python3
import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_instance_creation(self):
        """
        Test creating an instance of BaseModel.
        """
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)

    def test_attributes(self):
        """
        Test setting attributes and checking if they are present.
        """
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

        self.assertEqual(my_model.name, "My First Model")
        self.assertEqual(my_model.my_number, 89)

    def test_str_representation(self):
        """
        Test the __str__ representation of BaseModel.
        """
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

        expected_str = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), expected_str)

    def test_save_method(self):
        """
        Test the save method to update the 'updated_at' attribute.
        """
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        my_model.save()

        self.assertNotEqual(my_model.updated_at, initial_updated_at)

    def test_to_dict_method(self):
        """
        Test the to_dict method to get a dictionary representation.
        """
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

        model_dict = my_model.to_dict()

        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('id', model_dict)
        self.assertIn('name', model_dict)
        self.assertIn('my_number', model_dict)

if __name__ == '__main__':
    unittest.main()

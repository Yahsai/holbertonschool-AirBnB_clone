#!/usr/bin/python3
"""
This module defines the FileStorage class for serializing/deserializing instances to/from JSON.
"""

import json
from os import path

class FileStorage:
    """
    FileStorage class for serializing/deserializing instances to/from JSON.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as json_file:
            json.dump(obj_dict, json_file)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the file exists)."""
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding="utf-8") as json_file:
                obj_dict = json.load(json_file)
            for key, value in obj_dict.items():
                class_name, obj_id = key.split('.')
                obj_instance = eval(class_name)(**value)
                self.__objects[key] = obj_instance

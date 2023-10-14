#!/usr/bin/env python3
"""serializing and deserializing module
"""

import json
import os


class FileStorage:
    """serializes instances to a JSON file and deserializes JSON file to
    instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects
        """

        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id
        """

        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)
        """

        dictionary = {}

        for key, val in FileStorage.__objects.items():
            dictionary[key] = val.to_dict()

        with open(FileStorage.__file_path, "w") as file:
            json.dump(dictionary, file)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised
        """

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place

        dictionary = {'BaseModel': BaseModel, 'User': User, 'State': State,
                      'City': City, 'Amenity': Amenity, 'Place': Place}

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as file:
                for key, val in json.load(file).items():
                    self.new(dictionary[val['__class__']](**val))

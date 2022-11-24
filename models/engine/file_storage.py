#!/usr/bin/python3
""" The json file storage """
import json
from models.base_model import BaseModel

class FileStorage():
    """ Create a file storage
    - serialize to JSON file and deserialize 
    JSON file to instances
    
    Args:
        class attributtes:
            __file_path: string json ti file (file.json)
            __objects: empty dictionary
        class methods:
            all: All in the dictionary
            new: Create a new key
            save: serializes __objects to JSON path
            reload: deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}
    class_dict = {"my_model": BaseModel}
    
    def all(self):
        """ return the dictionary objects """
        return (self.__objects)

    def new(self, obj):
        """ set in __objects the obj with key id """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """ Serialize __objects to the JSON file
        path: __file_path
        """
        obj_dict = {}

        for key, obj in self.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(obj.to_dict, f)

    def reload(self):
        """ Deserializes the JSON file to __objects 
            if the file doesn't exist: show no errors
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                new_obj_dict = json.load(f)
            for key, value in new_obj_dict.items():
                obj = self.class_dict[value['__class__']](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
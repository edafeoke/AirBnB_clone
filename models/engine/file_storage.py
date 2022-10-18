#!/usr/bin/python3
'''
file_storage module
'''

import json
from os.path import exists
from datetime import datetime
import models
from models.base_model import BaseModel


class FileStorage:
    """File Storage class"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        '''returns the dictionary __objects'''
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with
        key <obj class name>.id"""

        k = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[k] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_dict = {}
        for k, v in self.__objects.items():
            json_dict[k] = v.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            f.write(json.dumps(json_dict))

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ;"""

        file_exists = exists(self.__file_path)

        if file_exists:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                dict = json.loads(f.read())
                for k, value in dict.items():
                    cls = value["__class__"]
                    obj = eval(cls)(**value)
                    #self.__objects[k] = obj
                    self.new(obj)

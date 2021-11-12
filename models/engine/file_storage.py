#!/usr/bin/python3
'''
file_storage module
'''

import json
from os.path import exists
import models


class FileStorage:
    '''
    serializes instances to a JSON file and deserializes JSON file
    to instances

    Attributes (class):
        __file_path: path to json file
        __objects: dictionary containing all saved objects
    '''

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        '''
        Initialisation method
        '''
        super().__init__()

    def all(self):
        '''
        returns all objects as a dictionary
        '''
        return FileStorage.__objects

    def new(self, obj):
        '''
        sets in __objects the obj with key <obj class name>.id
        '''
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        '''
        serializes __objects to the JSON file (path: __file_path)
        '''
        json_str = json.dumps(self.__objects)

        with open(self.__file_path, "w") as f:
            f.write(json_str)

    def reload(self):
        '''
        deserializes the JSON file to __objects
        '''
        file_exists = exists(self.__file_path)
        if file_exists:
            with open(self.__file_path, 'r') as f:
                json_str = f.read()
                dictionary = json.loads(json_str)
                self.__objects = dictionary

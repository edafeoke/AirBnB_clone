#!/usr/bin/env python3
'''
base_model module
'''

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    '''
    defines all common attributes/methods for other classes
    '''

    def __init__(self, *args, **kwargs):
        '''
        Instantiation method
        '''

        if len(kwargs):
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        '''
        string representation of the current object
        '''
        classname = self.__class__.__name__
        print("[{}] ({}) {}".format(classname, self.id, self.to_dict()))

    def save(self):
        '''
        updates the public instance attribute updated_at with
        the current datetime
        '''

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''
        Returns a dictionary containing all keys/values of __dict__
        of the instance
        '''
        dictionary = {}
        for k, v in self.__dict__.items():
            dictionary[k] = v
        dictionary['__class__'] = type(self).__name__
        dictionary['created_at'] = datetime.isoformat(self.created_at)
        dictionary['updated_at'] = datetime.isoformat(self.updated_at)
        return dictionary

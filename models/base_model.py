#!/usr/bin/env python3
'''
base_model module
'''

import uuid
from datetime import datetime
import models


class BaseModel:
    '''
    defines all common attributes/methods for other classes
    '''

    def __init__(self, *args, **kwargs):
        '''
        Instatiation method
        '''

        if len(kwargs):
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        '''
        string representation of the current object
        '''
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)

    def save(self):
        '''
        updates the public instance attribute updated_at with
        the current datetime
        '''

        self.updated_at = datetime.now()
        models.storage.save()

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

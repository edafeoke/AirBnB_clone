#!/usr/bin/env python3
'''
base_model module
'''

import uuid
import datetime

class BaseModel:
    '''
    defines all common attributes/methods for other classes
    '''

    def __init__(self):
        '''
        Instatiation method
        '''

        self.id = uuid.uuid4()

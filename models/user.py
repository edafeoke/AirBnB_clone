#!/usr/bin/python3
'''
User module
'''

from models.base_model import BaseModel


class User(BaseModel):
    '''
    a class User that inherits from BaseModel
    '''

    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        '''
        init method
        '''
        super().__init__(*args, **kwargs)

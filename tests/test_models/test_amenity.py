#!/usr/bin/python3
'''
module containing User class tests
'''

import unittest
from models.amenity import Amenity


class TestUser(unittest.TestCase):
    '''
    Test class that tests the User class
    '''
    
    def test_instance(self):
        '''
        test form object
        '''
        obj = Amenity()
        self.assertIsInstance(obj, Amenity)

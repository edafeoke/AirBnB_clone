#!/usr/bin/python3
'''
module containing User class tests
'''

import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    '''
    Test class that tests the Amenity class
    '''
    def setUp(self):
        '''
        test form object
        '''
        obj = Amenity()
        obj.name = "water"

    def test_attributes(self):
        '''
        test all attributes
        '''
        self.assertIsInstance(obj, Amenity, "")
        self.assertIs(obj.name, "water")


if __name__ == '__main__':
    unittest.main()

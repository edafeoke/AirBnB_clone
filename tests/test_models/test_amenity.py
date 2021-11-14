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
    
    def test_instance(self):
        '''
        test form object
        '''
        obj = Amenity()
        self.assertIsInstance(obj, Amenity, "")

if __name__ == '__main__':
    unittest.main()

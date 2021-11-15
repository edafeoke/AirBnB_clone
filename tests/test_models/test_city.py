#!/usr/bin/python3
'''
module containing User class tests
'''

import unittest
from models.city import City


class TestUser(unittest.TestCase):
    '''
    Test class that tests the User class
    '''

    def setUp(self):
        '''
        Test iinstance of city class
        '''
        obj = City()
        obj.name = "Asaba"

    def test_attributes(self):
        '''
        test all attr
        '''
        self.assertIsInstance(obj, City, "")
        self.assertIs(obj.name, "Asaba")


if __name__ == '__main__':
    unittest.main()

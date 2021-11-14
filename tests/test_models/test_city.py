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

    def test_instance(self):
        '''
        Test iinstance of city class
        '''
        obj = City()
        self.assertIsInstance(obj, City, "")

if __name__ == '__main__':
    unittest.main()

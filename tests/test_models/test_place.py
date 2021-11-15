#!/usr/bin/python3
'''
module containing Place class tests
'''

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    '''
    Test class that tests the Place class
    '''

    def setUp(self):
        '''
        test instance of class
        '''
        obj = Place()
        obj.name = "work"

    def test_attributes(self):
        '''
        docs
        '''
        self.assertIsInstance(obj, Place, "")
        self.assertIs(obj.name, "work")

if __name__ == '__main__':
    unittest.main()

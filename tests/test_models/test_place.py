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

    def test_instance(self):
        '''
        test instance of class
        '''
        obj = Place()
        self.assertIsInstance(obj, Place, "")

if __name__ == '__main__':
    unittest.main()

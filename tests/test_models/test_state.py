#!/usr/bin/python3
'''
module containing User class tests
'''

import unittest
from models.state import State


class TestState(unittest.TestCase):
    '''
    Test class that tests the User class
    '''

    def setUp(self):
        '''
        test instance
        '''
        obj = State()
        obj.name = "Delta"

    def test_attr(self):
        '''
        docs
        '''
        self.assertIs(obj.name, "Delta")
        self.assertIsInstance(obj, State, "")

if __name__ == "__main__":
    unittest.main()

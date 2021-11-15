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

    def test_instance(self):
        '''
        test instance
        '''
        obj = State()
        self.assertIsInstance(obj, State, "")


if __name__ == "__main__":
    unittest.main()

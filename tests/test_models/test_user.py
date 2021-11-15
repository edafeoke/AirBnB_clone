#!/usr/bin/python3
'''
module containing User class tests
'''

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    '''
    Test class that tests the User class
    '''

    def test_instance(self):
        '''
        Test for instance of User class
        '''
        obj = User()
        self.assertIsInstance(obj, User, "")


if __name__ == '__main__':
    unittest.maiin()

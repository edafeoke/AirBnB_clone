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

    def setUp(self):
        '''
        Setup test method
        '''
        user = User()
        user.name = "Edafe Oke"
        user.email = "greatedafeoke@gmail.com"

    def test_attributes(self):
        '''
        test all attributes
        '''
        self.assertIs(user.name, "Edafe Oke")
        self.assertIs(user.email, "greatedafeoke@gmail.com")

if __name__ == '__main__':
    unittest.main()

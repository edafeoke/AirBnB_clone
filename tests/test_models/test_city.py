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
    obj = City()
    self.assertIsInstance(obj, City)

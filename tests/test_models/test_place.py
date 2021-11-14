#!/usr/bin/python3
'''
module containing User class tests
'''

import unittest
from models.place import Place


class TestUser(unittest.TestCase):
    '''
    Test class that tests the User class
    '''
    obj = Place()
    self.assertIsInstance(obj, Place)

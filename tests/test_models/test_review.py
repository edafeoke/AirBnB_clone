#!/usr/bin/python3
'''
module containing User class tests
'''

import unittest
from models.review import Review


class TestUser(unittest.TestCase):
    '''
    Test class that tests the User class
    '''
    obj = Review()
    self.assertIsInstance(obj, Review)

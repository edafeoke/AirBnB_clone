#!/usr/bin/python3
'''
A unittest test module for the base_model module
'''

import unittest
from models.base_model import BaseModel
import models


class TestBaseModel(unittest.TastCase):
    '''
    A test class that inherits unittest.TestCase
    '''

    def __init__(self):
        self.model = BaseModel()

    def setUp(self):
        '''
        Set up test class
        '''
        self.model = BaseModel()
        return super().setup()

    def tearDown(self):
        '''
        Tear down test class
        '''
        self.model.dispose()
        return super().tearDown()

    def test_init(self):
        '''
        Test instantiation
        '''
        self.assertIsInstance(self.model, BaseModel)

    def test_attributes(self):
        '''
        Test for class and objects attribute
        '''
        self.model.my_number = 1
        self.model.name = "Model 1"
        self.assertEqual(self.model.name, "Model 1")
        self.assertEqual(self.model.my_number, 1)


if __name__ == '__main__':

    unittest.main()

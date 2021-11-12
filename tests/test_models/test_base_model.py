#!/usr/bin/python3
'''
Module for base_model unittest
'''

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''
    Test BaseModel class
    '''
    
    model = BaseModel()
    model.name = "Knightess"

    def setUp(self):
        '''
        Setup class
        '''
        model = BaseModel()
        model.name = "Knightess"
        model.number = 28

    def tearDown(self):
        '''
        Cleans up after test methods
        '''
        pass

    def test_has_attribute(self):
        '''
        Test if instance has all attributes
        '''
        model = BaseModel()
        model.name = "Knightess"
        model.number = 28
        self.assertTrue(hasattr(model, "id"))
        self.assertTrue(hasattr(model, "created_at"))
        self.assertTrue(hasattr(model, "updated_at"))
        self.assertTrue(hasattr(model, "name"))
        self.assertTrue(hasattr(model, "number"))

    def test_attribute_type(self):
        '''
        Test for all attribute types
        '''
        model = BaseModel()
        self.assertIs(type(model.created_at), datetime)

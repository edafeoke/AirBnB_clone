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
        self.assertIs(type(model.updated_at), datetime)
        self.assertIs(type(model.id), str)


    def test_from_dict(self):
        '''
        Test whether BaseModel correctly create object from dictionary
        '''

        dictionary = {
                'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                'created_at': '2017-09-28T21:03:54.052298',
                '__class__': 'BaseModel',
                'my_number': 89,
                'updated_at': '2017-09-28T21:03:54.052302',
                'name': 'My_First_Model'
                }
        cdate = datetime(2017, 9, 28, 21, 3, 54, 52298)
        udate = datetime(2017, 9, 28, 21, 3, 54, 52302)
        model = BaseModel(**dictionary)
        self.assertIs(model.id, '56d43177-cc5f-4d6c-a0c1-e167f8c27337')
        self.assertIs(model.name, "My_First_Model")
        self.assertIs(model.my_number, 89)
        self.assertEqual(model.created_at, cdate)
        self.assertEqual(model.updated_at, udate)


if __name__ == "__main__":
    unittest.main()
